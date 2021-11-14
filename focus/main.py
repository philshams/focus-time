import numpy as np
from playsound import playsound
from pathlib import Path
from focus.timer import Timer

class Focus():
    def __init__(self):
        self.test_speakers()

    def session(self, context: str='single session'):
        self.query_intended_minutes_focus()
        self.run_timer()
        self.report_outcome_of_session(context)

    def day(self):
        self.hours_of_focus, self.session_num = 0, 0
        self.query_intended_hours_of_focus()
        while self.hours_of_focus < self.intended_hours_of_focus:
            self.report_hours_of_focus_remaining()
            self.session(context='part of a focus day')
            self.hours_of_focus += self.mins_focused_in_session / 60
        self.report_outcome_of_day()

# -----SESSION FUNCTIONS--------------------------------------------------------------------------- 
    def query_intended_minutes_focus(self):
        self.intended_mins_focus = float(input('\n-- How long would you like to focus for? (minutes)          '))

    def run_timer(self):
        self.mins_focused_in_session, self.session_failed = Timer(self.intended_mins_focus).time_session(self.sound)

    def report_outcome_of_session(self, context):
        if context == 'part of a focus day': return
        if self.session_failed: 
            print('Out of time.')
            if self.sound: playsound(str(Path(__file__).parent / '../data/failure.mp3'))
        elif not self.session_failed:
            print('You did it!!!')
            if self.sound: playsound(str(Path(__file__).parent / '../data/success.mp3'))

# -----DAY FUNCTIONS-------------------------------------------------------------------------------
    def query_intended_hours_of_focus(self):
        self.intended_hours_of_focus = float(input('\n-- How long would you like to focus for today? (hours)          '))            

    def report_hours_of_focus_remaining(self):
        self.hours_of_focus_left = self.intended_hours_of_focus - self.hours_of_focus
        less_than_two_hours_left = self.hours_of_focus_left < 2
        self.session_num += 1
        print(f"\n   You only have {np.round(self.hours_of_focus_left*(1 + 59*less_than_two_hours_left),1)} {'minutes'*less_than_two_hours_left + 'hours'*~less_than_two_hours_left} to go. When you're ready, let's start session number {self.session_num}!\n")

    def report_outcome_of_day(self):
        if np.random.random() < .95:
            print('\nCongratulations slugger, you have just scored a day of focus!\n')
            if self.sound: playsound(str(Path(__file__).parent / '../data/home run.mp3'))
        else:
            print('\nYaaaaaaay. Another day of focus!\n')
            if self.sound: playsound(str(Path(__file__).parent / '../data/yay.mp3'))
# -----INIT FUNTIONS------------------------------------------------------------------------------
    def test_speakers(self):
        try: 
            playsound(str(Path(__file__).parent / '../data/test.mp3'))
            self.sound = True
        except Exception: 
            print('Note: speakers not identified, sound will not play')
            self.sound = False