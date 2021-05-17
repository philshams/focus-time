from focus.session import focus_session
from playsound import playsound
from pathlib import Path
import numpy as np

def focus_day():
    '''      FOCUS TIMER for multiple sessions over one day      '''
    target_focus_duration =         float(input('How long would you like to focus for today? (hours)          '))

    session_number = 1
    time_focused_day = 0

    while time_focused_day < target_focus_duration:
        time_left = target_focus_duration - time_focused_day
        if time_left < 1:
            print("\nYou have {} minutes to go. When you're ready let's start session number {}!\n".format(np.round(time_left*60,1), session_number))
        else:
            print("\nYou have {} hours to go. When you're ready let's start session number {}!\n".format(np.round(time_left,1), session_number))
        time_focused_session = focus_session() # run the focus session
        time_focused_day += (time_focused_session/60)
        session_number += 1
    
    print('\nCongratulations slugger, you have just scored a day of focus!')
    random_number = np.random.random()
    if random_number < .95:
        playsound(str(Path(__file__).parent / '../data/home run.mp3'))
    else: # once every twenty days, play this instead
        playsound(str(Path(__file__).parent / '../data/yay.mp3'))

if __name__ == "__main__":
    focus_day()