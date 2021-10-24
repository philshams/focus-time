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
        self.intended_mins_of_focus    = intended_mins_of_focus
        self.secs_left_in_session      = self.intended_mins_of_focus*60
        self.minute_timer_start_time   = time.time()
        self.reminder_duration_secs    = 15
        self.session_failed            = False
        self.set_max_session_duration()
        self.set_interval_between_focus_reminders()

    def time_session(self) -> Tuple[float, bool]:
        self.initiate_session()
        while self.secs_left_in_session > 0:
            self.select_secs_between_reminders()
            self.wait_until_next_reminder()
            if self.session_failed: break
            self.issue_reminder()
        mins_focused_in_session = self.intended_mins_of_focus - self.secs_left_in_session/60
        return mins_focused_in_session, self.session_failed

# ------INIT FUNCS-------------------------------------------
    def set_max_session_duration(self):
        if   self.intended_mins_of_focus <= 5:  self.max_mins_in_session = 10.
        elif self.intended_mins_of_focus <= 15: self.max_mins_in_session = self.intended_mins_of_focus * 2
        elif self.intended_mins_of_focus < 20:  self.max_mins_in_session = 30.
        elif self.intended_mins_of_focus >= 20: self.max_mins_in_session = self.intended_mins_of_focus * 1.5 

    def set_interval_between_focus_reminders(self):
        if   self.intended_mins_of_focus > 2:  self.avg_secs_between_reminders = np.sqrt(self.intended_mins_of_focus) * 60
        elif self.intended_mins_of_focus <= 2: self.avg_secs_between_reminders = self.intended_mins_of_focus / 2 * 60

        self.min_secs_between_reminders = min(20, self.avg_secs_between_reminders/2)
        self.max_secs_between_reminders = self.avg_secs_between_reminders*2

# -----TIME_SESSION FUNCS--------------------------------------
    def initiate_session(self):
        self.session_start_time      = time.time()
        print('\n-- Starting focus session for {} minutes of quality time (up to {} minutes of real time)       {}\n\n'.\
              format(self.intended_mins_of_focus, self.max_mins_in_session, datetime.now()))
        playsound(str(Path(__file__).parent / '../data/start.mp3'))

    def select_secs_between_reminders(self):
        self.secs_between_reminders = -np.inf
        while self.secs_between_reminders < self.min_secs_between_reminders or self.secs_between_reminders > self.max_secs_between_reminders:
            exponential_dist_scale = self.avg_secs_between_reminders - self.min_secs_between_reminders
            self.secs_between_reminders = np.random.exponential(scale = exponential_dist_scale) + self.min_secs_between_reminders

    def wait_until_next_reminder(self):
        last_reminder_time          = time.time()
        secs_elapsed_since_reminder = 0
        while secs_elapsed_since_reminder < self.secs_between_reminders:
            secs_elapsed_since_reminder  = time.time() - last_reminder_time
            self.secs_elapsed_in_session = time.time() - self.session_start_time
            self.mins_elapsed_in_session = self.secs_elapsed_in_session / 60
            self.print_line_break_each_minute() 
            if self.time_is_up():
                self.user_failed()
                break
        self.secs_left_in_session -= (self.secs_between_reminders + self.reminder_duration_secs)

    def time_is_up(self) -> bool:
        if self.mins_elapsed_in_session > self.max_mins_in_session:  return True
        if self.mins_elapsed_in_session <= self.max_mins_in_session: return False

    def user_failed(self):
        print('Out of time.')
        playsound(str(Path(__file__).parent / '../data/failure.mp3'))
        self.session_failed = True
    
    def print_line_break_each_minute(self):
        if int(self.secs_elapsed_in_session) % 60 == 0 and int(self.secs_elapsed_in_session) > 0: 
            self.minute_timer_start_time = time.time()
            print('')

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
        print('Were you focusing? If yes, carry on. If no, press any key within {} seconds'.format(self.reminder_duration_secs));
        playsound(str(Path(__file__).parent / '../data/ding dong.mp3'))
        while True:
            if self.key_pressed: return False # any key is pressed
            if (time.time() - start_time) > self.reminder_duration_secs: return True

    def key_pressed(self) -> bool:
        if sys.platform[:3]=='win':       
            return msvcrt.kbhit()
        else:
            return sys.stdin.read(1)