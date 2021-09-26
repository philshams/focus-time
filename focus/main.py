import numpy as np
from playsound import playsound
from pathlib import Path
from focus.timer import timer

class Focus():
    def init(self):
        self.hours_of_focus_done = 0
        self.sessions_done = 0

    def day(self):
        self.ask_user_intended_hours_of_focus()
        while self.hours_of_focus_done < self.intended_hours_of_focus:
            self.report_hours_of_focus_remaining()
            self.session(context='day')
            self.hours_of_focus_done += self.hours_focused_in_that_session
        self.celebrate_a_successful_day()
    
    def session(self, context: str='just one session'):
        self.ask_user_intended_minutes_of_focus()
        self.run_timer()
        if context == 'just one session':
            self.celebrate_a_successful_session()

# -----DAY FUNCTIONS-------------------------------------------------------------------------------
    def ask_user_intended_hours_of_focus(self):
        self.intended_hours_of_focus = float(input('How long would you like to focus for today? (hours)          '))            

    def report_hours_of_focus_remaining(self):
        self.hours_of_focus_left = self.intended_hours_of_focus - self.hours_of_focus_done
        if self.hours_of_focus_left < 1: 
            print("\nYou only have {} minutes to go. When you're ready, let's start session number {}!\n".format(np.round(self.hours_of_focus_left*60,1), self.session_number))
        elif self.hours_of_focus_left >=1: 
            print("\nYou have {} hours to go. When you're ready, let's start session number {}!\n".format(np.round(self.hours_of_focus_left,1), self.session_number))

    def celebrate_a_successful_day(self):
        if np.random.random() < .95:
            print('\nCongratulations slugger, you have just scored a day of focus!\n')
            playsound(str(Path(__file__).parent / '../data/home run.mp3'))
        else:
            print('\nYaaaaaaay. Another day of focus!\n')
            playsound(str(Path(__file__).parent / '../data/yay.mp3'))

# -----SESSION FUNCTIONS--------------------------------------------------------------------------- 
    def ask_user_intended_minutes_of_focus(self):
        self.intended_mins_of_focus = float(input('How long would you like to focus for? (minutes)          '))

    def run_timer(self):
        self.hours_focused_in_that_session, self.session_failed = Timer(self)
        self.sessions_done += 1

    def celebrate_a_successful_session(self):
        if self.session_failed: return
        print('You did it!!!')
        playsound(str(Path(__file__).parent / '../data/success.mp3'))