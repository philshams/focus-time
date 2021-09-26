import numpy as np
import time
from playsound import playsound
import msvcrt
from datetime import datetime
from pathlib import Path

    # def set_max_mins_in_session(self) -> None:
    #     if   self.intended_minutes_of_focus <= 5:  self.max_mins_in_session = 10.
    #     elif self.intended_minutes_of_focus <= 15: self.max_mins_in_session = self.intended_mins_of_focus * 2
    #     elif self.intended_minutes_of_focus < 20:  self.max_mins_in_session = 30.
    #     elif self.intended_minutes_of_focus >= 20: self.max_mins_in_session = self.intended_mins_of_focus * 1.5 

    # def set_interval_between_focus_reminders(self):
    #     if self.intended_mins_of_focus > 2:    self.avg_secs_between_reminders = np.sqrt(self.intended_mins_of_focus) * 60
    #     elif self.intended_mins_of_focus <= 2: self.avg_secs_between_reminders = self.intended_mins_of_focus / 2 * 60
    #     self.min_secs_between_reminders = min(20, self.avg_secs_between_reminders/2)
    #     self.max_secs_between_reminders = self.avg_secs_between_reminders*2

def timer(target_focus_duration, maximum_session_duration, average_interval, minimum_interval, maximum_interval, minutes_required):  
    print(datetime.now())
    print('\nstarting focus session for {} to {} minutes\n'.format(target_focus_duration, maximum_session_duration))
    playsound(str(Path(__file__).parent / '../data/start.mp3'))
    # how much time is left
    focus_time_left = target_focus_duration*60
    # set a timer for the whole session
    session_start_time = time.time()
    minute_timer_start_time = time.time()
    failed = False
    # Start the main loop
    while focus_time_left > 0:
        # Select the interval between reminders (ding dong sound)
        interval = -1
        while interval < minimum_interval or interval > maximum_interval:
            interval = np.random.exponential(scale = (average_interval - minimum_interval)) + minimum_interval
        # Wait for the interval to pass
        interval_start_time = time.time()
        interval_time_elapsed = 0
        while interval_time_elapsed < interval:
            minute_timer_time_elapsed = time.time() - minute_timer_start_time
            interval_time_elapsed = time.time() - interval_start_time
            total_time_elapsed = time.time() - session_start_time
            if int(minute_timer_time_elapsed) > 0 and int(minute_timer_time_elapsed) % 60 == 0: 
                minute_timer_start_time = time.time()
                print('')
            if total_time_elapsed > maximum_session_duration*60:
                print('Out of time.')
                playsound(str(Path(__file__).parent / '../data/failure.mp3'))
                failed = True
                break

        if failed:
            break
        else:  
            ans = focus_query('Were you focusing? If yes, carry on. If no, press any key within 10 seconds', timeout = 10) 
            if ans:
                print('\nGreat job!')
                focus_time_left -= (interval+10)
                print(str(np.round(100-100*focus_time_left / (target_focus_duration*60))) + '% done\n')
            else:
                print('Keep at it, champ\n')

    time_focused_session = (target_focus_duration - (focus_time_left/60)) # in minutes

    if not failed:
        if time_focused_session < minutes_required: # skip this if you've passed the focus day
            print('You did it!!!')
            playsound(str(Path(__file__).parent / '../data/success.mp3'))

    return time_focused_session
    
def focus_query(caption, timeout = 5):
    start_time = time.time()
    while msvcrt.kbhit(): msvcrt.getche() # Remove keys pressed in the interval
    print(caption);
    playsound(str(Path(__file__).parent / '../data/ding dong.mp3'))
    while True: # If a key is pressed, return False; otherwise True
        if msvcrt.kbhit(): return False
        if (time.time() - start_time) > timeout: return True