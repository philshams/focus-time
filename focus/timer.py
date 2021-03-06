import numpy as np
import time
import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from datetime import datetime
from pathlib import Path
from typing import Tuple
import sys
if sys.platform[:3]=='win': 
    from msvcrt import kbhit as key_pressed_windows, getch as clear_keypresses
else: 
    from tty import setcbreak as hide_user_input_from_terminal
    import termios
    import io
    import signal

class Timer():
    def __init__(self, intended_mins_focus):
        ''' note: units of time are all in secs unless called 'mins' '''
        self.intended_mins_of_focus = intended_mins_focus
        self.mins_focused_so_far    = 0
        self.duration_of_reminder   = 15
        self.keyboard               = True # if key input fails, this changes to false
        self.calculate_max_session_duration()
        self.calculate_inter_reminder_interval_parameters()
        self.initialize_timer_sounds()        

    def time_session(self, sound=True) -> Tuple[float, bool]:
        self.initiate_session(sound)
        while self.mins_focused_so_far < self.intended_mins_of_focus:
            self.select_inter_reminder_interval()
            self.wait_until_next_reminder()
            if self.session_timed_out: break
            self.issue_reminder()
        return self.mins_focused_so_far, self.session_timed_out

# ------INIT FUNCS-------------------------------------------
    def calculate_max_session_duration(self):
        if   self.intended_mins_of_focus <= 5:  self.max_mins_in_session = 10.
        elif self.intended_mins_of_focus <= 15: self.max_mins_in_session = self.intended_mins_of_focus * 2
        elif self.intended_mins_of_focus < 20:  self.max_mins_in_session = 30.
        elif self.intended_mins_of_focus >= 20: self.max_mins_in_session = self.intended_mins_of_focus * 1.5 

    def calculate_inter_reminder_interval_parameters(self):
        ''' get the min, max, and scale of an exponential dist which is sampled to produce each inter-reminder interval '''
        if   self.intended_mins_of_focus >  2: self.avg_inter_reminder_interval = int(np.sqrt(self.intended_mins_of_focus) * 60)
        elif self.intended_mins_of_focus <= 2: self.avg_inter_reminder_interval = int(max(30, self.intended_mins_of_focus / 2 * 60))
        self.min_inter_reminder_interval = min(20, int(self.avg_inter_reminder_interval/2))
        self.max_inter_reminder_interval = self.avg_inter_reminder_interval*2
        self.exponential_parameter = self.avg_inter_reminder_interval - self.min_inter_reminder_interval

# -----TIME_SESSION FUNCS--------------------------------------
    def initiate_session(self, sound = True):
        print(f'\n-- Starting focus session for {self.intended_mins_of_focus} minute{"" + "s"*(self.intended_mins_of_focus!=1)} of quality time (up to {int(self.max_mins_in_session)} minutes of real time)\n   {datetime.now()}\n')
        self.sound = sound # speakers working
        if self.sound: pygame.mixer.Sound.play(self.start_mp3)
        self.session_start_time = time.time()

    def select_inter_reminder_interval(self):
        self.inter_reminder_interval = -np.inf
        while self.inter_reminder_interval < self.min_inter_reminder_interval or self.inter_reminder_interval > self.max_inter_reminder_interval:
            self.inter_reminder_interval = np.random.exponential(scale = self.exponential_parameter) + self.min_inter_reminder_interval

    def wait_until_next_reminder(self):
        start_time = time.time()
        while (time.time() - start_time) < self.inter_reminder_interval:
            time.sleep(1)
            self.mins_elapsed_in_session = (time.time() - self.session_start_time) / 60
            if self.time_is_up(): break
        
    def time_is_up(self) -> bool:
        if self.mins_elapsed_in_session > self.max_mins_in_session: 
            self.session_timed_out = True
        else:
            self.session_timed_out = False
        return self.session_timed_out        

    def issue_reminder(self):
        self.disregard_keys_pressed_during_inter_reminder_interval()
        print(f'-- Were you focusing? If yes, carry on. If no, press any key within {self.duration_of_reminder} seconds')
        if self.sound: pygame.mixer.Sound.play(self.reminder_mp3)
        user_pressed_key = self.get_user_response()
        if not user_pressed_key:
            self.mins_focused_so_far += (self.inter_reminder_interval + self.duration_of_reminder) / 60
            print(f'   Great job! {min(100, int(self.mins_focused_so_far / self.intended_mins_of_focus * 100))}% complete\n')
        elif user_pressed_key:
            print(f'   Keep at it, champ. Still at {int(self.mins_focused_so_far / self.intended_mins_of_focus * 100)}%\n')

    def get_user_response(self) -> bool:
        if not self.keyboard: return
        if sys.platform[:3]=='win':
            return self.get_keypress_windows()
        else: #unix systems - interrupt stdin after reminder duration
            signal.signal(signal.SIGALRM, self.unix_timeout)
            signal.alarm(self.duration_of_reminder)
            user_pressed_key = self.get_keypress_unix()
            signal.alarm(0)
            return user_pressed_key

    def get_keypress_windows(self)->bool:
        start_time = time.time()
        while (time.time() - start_time) < self.duration_of_reminder:
            time.sleep(1)
            if key_pressed_windows():
                return True # if a key is pressed

    def get_keypress_unix(self) -> bool:
        try:
            stdin_file = sys.stdin.fileno()
            original_terminal_settings = termios.tcgetattr(stdin_file)
            hide_user_input_from_terminal(sys.stdin)
            user_pressed_key = sys.stdin.read(1)
            termios.tcsetattr(stdin_file, termios.TCSADRAIN, original_terminal_settings) # restore input settings
            return user_pressed_key
        except BlockingIOError:
            termios.tcsetattr(stdin_file, termios.TCSADRAIN, original_terminal_settings)
            return False
        except io.UnsupportedOperation:
            self.keyboard = False
            print('keyboard not identified')
        

    def unix_timeout(self, *args):
        raise BlockingIOError()

    def disregard_keys_pressed_during_inter_reminder_interval(self):
        if not self.keyboard: return
        if sys.platform[:3]=='win':
            while key_pressed_windows(): 
               clear_keypresses()
        else:   
            try:
                termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            except (io.UnsupportedOperation, termios.error):
                self.keyboard = False
                print('keyboard not identified')

    def initialize_timer_sounds(self):
        try:
            pygame.mixer.init()
            self.start_mp3    = pygame.mixer.Sound(str(Path(__file__).parent / '../data/start.wav'))
            self.reminder_mp3 = pygame.mixer.Sound(str(Path(__file__).parent / '../data/ding dong.mp3'))
        except pygame.error: 
            pass # this code is also executed in the main script, so leave out speaker error message here