import numpy as np
import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
from pathlib import Path
from focus.timer import Timer

class Focus():
    def __init__(self):
        self.initialize_focus_sounds()

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
        try:
            self.intended_mins_focus = float(input('\n-- How long would you like to focus for? (minutes)          '))
        except ValueError:
            print('please enter a number!')
            self.query_intended_minutes_focus()

    def run_timer(self):
        self.mins_focused_in_session, self.session_failed = Timer(self.intended_mins_focus).time_session(self.sound)

    def report_outcome_of_session(self, context):
        if self.session_failed: 
            print('Out of time.')
            if self.sound: 
                pygame.mixer.Sound.play(self.session_failure_mp3)
                time.sleep(self.session_failure_mp3.get_length())
        elif context == 'single session' and not self.session_failed:
            print('You did it!!!')
            if self.sound: pygame.mixer.Sound.play(self.session_success_mp3)
            time.sleep(self.session_success_mp3.get_length())
        elif context == 'part of a focus day' and not self.session_failed:
            print('Session complete')
            if self.sound: pygame.mixer.Sound.play(self.session_complete_mp3)
            time.sleep(self.session_complete_mp3.get_length())

# -----DAY FUNCTIONS-------------------------------------------------------------------------------
    def query_intended_hours_of_focus(self):
        try:
            self.intended_hours_of_focus = float(input('\n-- How long would you like to focus for today? (hours)          '))  
        except ValueError:
            print('please enter a number!')
            self.query_intended_minutes_focus()
                  

    def report_hours_of_focus_remaining(self):
        self.hours_of_focus_left = self.intended_hours_of_focus - self.hours_of_focus
        less_than_two_hours_left = self.hours_of_focus_left < 2
        self.session_num += 1
        print(f"\n   You only have {np.round(self.hours_of_focus_left*(1 + 59*less_than_two_hours_left),1)} {'minutes'*less_than_two_hours_left + 'hours'*~less_than_two_hours_left} to go. When you're ready, let's start session number {self.session_num}!\n")

    def report_outcome_of_day(self):
        if np.random.random() < .95:
            print('\nCongratulations, you have just achieved a day of focus!\n')
            if self.sound: 
                pygame.mixer.Sound.play(self.day_success_mp3_I)
                time.sleep(self.day_success_mp3_I.get_length())
        else:
            print('\nYaaaaaaay. Another day of focus!\n')
            if self.sound: 
                pygame.mixer.Sound.play(self.day_success_mp3_II)
                time.sleep(self.day_success_mp3_II.get_length())
# -----INIT FUNTIONS------------------------------------------------------------------------------
    def initialize_focus_sounds(self):
        try: 
            pygame.mixer.init()
            sound_check_mp3 = pygame.mixer.Sound(str(Path(__file__).parent / '../data/test.mp3'))
            sound_check_wav = pygame.mixer.Sound(str(Path(__file__).parent / '../data/test.wav'))
            pygame.mixer.Sound.play(sound_check_mp3)
            pygame.mixer.Sound.play(sound_check_wav)
            self.session_success_mp3  = pygame.mixer.Sound(str(Path(__file__).parent / '../data/success.mp3'))
            self.session_failure_mp3  = pygame.mixer.Sound(str(Path(__file__).parent / '../data/failure.wav'))
            self.session_complete_mp3 = pygame.mixer.Sound(str(Path(__file__).parent / '../data/session complete.mp3'))
            self.day_success_mp3_I    = pygame.mixer.Sound(str(Path(__file__).parent / '../data/victory.mp3'))
            self.day_success_mp3_II   = pygame.mixer.Sound(str(Path(__file__).parent / '../data/yay.mp3'))
            self.start_mp3            = pygame.mixer.Sound(str(Path(__file__).parent / '../data/start.wav'))
            self.reminder_mp3         = pygame.mixer.Sound(str(Path(__file__).parent / '../data/ding dong.mp3'))
            self.sound = True
        except pygame.error: 
            print('Note: speakers not identified, sound will not playaa')
            self.sound = False