import numpy as np
import time
from playsound import playsound
from datetime import datetime
from pathlib import Path
from typing import Tuple
import sys
if sys.platform[:3]=='win':  import msvcrt
else:                      import tty



class Timer():
    def __init__(self, intended_mins_of_focus):
        ''' note: units of time are all in secs unless called 'mins' '''
        self.intended_mins_of_focus = intended_mins_of_focus
        self.mins_focused_so_far    = 0
        self.duration_of_reminder   = 15
        self.calculate_max_session_duration()
        self.calculate_inter_reminder_interval_parameters()

    def time_session(self) -> Tuple[float, bool]:
        self.initiate_session()
        while self.mins_focused_so_far < self.intended_mins_of_focus:
            self.select_inter_reminder_interval()
            self.wait_until_next_reminder()
            if self.session_failed: break
            self.issue_reminder()
        return self.mins_focused_so_far, self.session_failed

# ------INIT FUNCS-------------------------------------------
    def calculate_max_session_duration(self):
        if   self.intended_mins_of_focus <= 5:  self.max_mins_in_session = 10.
        elif self.intended_mins_of_focus <= 15: self.max_mins_in_session = self.intended_mins_of_focus * 2
        elif self.intended_mins_of_focus < 20:  self.max_mins_in_session = 30.
        elif self.intended_mins_of_focus >= 20: self.max_mins_in_session = self.intended_mins_of_focus * 1.5 

    def calculate_inter_reminder_interval_parameters(self):
        ''' get the min, max, and scale of an exponential dist which is sampled to produce each inter-reminder interval '''
        if   self.intended_mins_of_focus > 2:  self.avg_secs_between_reminders = np.sqrt(self.intended_mins_of_focus) * 60
        elif self.intended_mins_of_focus <= 2: self.avg_secs_between_reminders = self.intended_mins_of_focus / 2 * 60
        self.min_secs_between_reminders = min(20, self.avg_secs_between_reminders/2)
        self.max_secs_between_reminders = self.avg_secs_between_reminders*2
        self.exponential_parameter = self.avg_secs_between_reminders - self.min_secs_between_reminders

# -----TIME_SESSION FUNCS--------------------------------------
    def initiate_session(self):
        print(f'\n-- Starting focus session for {int(self.intended_mins_of_focus)} minute{"" + "s"*(self.intended_mins_of_focus!=1)} of quality time (up to {int(self.max_mins_in_session)} minutes of real time)\n   {datetime.now()}\n\n')
        playsound(str(Path(__file__).parent / '../data/start.mp3'))
        self.session_start_time = time.time()

    def select_inter_reminder_interval(self):
        self.inter_reminder_interval = -np.inf
        while self.inter_reminder_interval < self.min_secs_between_reminders or self.inter_reminder_interval > self.max_secs_between_reminders:
            self.inter_reminder_interval = np.random.exponential(scale = self.exponential_parameter) + self.min_secs_between_reminders

    def wait_until_next_reminder(self):
        start_time = time.time()
        while (time.time() - start_time) < self.inter_reminder_interval:
            self.mins_elapsed_in_session = (time.time() - self.session_start_time) / 60
            if self.time_is_up(): break
        self.mins_focused_so_far += (self.inter_reminder_interval + self.duration_of_reminder) / 60

    def time_is_up(self) -> bool:
        if self.mins_elapsed_in_session > self.max_mins_in_session: 
            self.session_failed = True
        else:
            self.session_failed = False
        return self.session_failed        

    def issue_reminder(self):
        user_is_focusing = self.focus_query() 
        if user_is_focusing:
            percent_of_session_completed = np.round(100 - 100 * self.mins_elapsed_in_session / self.intended_mins_of_focus)
            print('\nGreat job!\n{}% done\n'.format(percent_of_session_completed))
        if not user_is_focusing:
            print('Keep at it, champ\n')

    def focus_query(self) -> bool:
        start_time = time.time()
        if sys.platform[:3]=='win':   
            while msvcrt.kbhit(): msvcrt.getche() # disregard keys pressed in the inter-reminder interval
        else:
            tty.setcbreak(sys.stdin)
        print('Were you focusing? If yes, carry on. If no, press any key within {} seconds'.format(self.duration_of_reminder));
        playsound(str(Path(__file__).parent / '../data/ding dong.mp3'))
        while True:
            if self.key_pressed: return False # any key is pressed
            if (time.time() - start_time) > self.duration_of_reminder: return True

    def key_pressed(self) -> bool:
        if sys.platform[:3]=='win':       
            return msvcrt.kbhit()
        else:
            return sys.stdin.read(1)