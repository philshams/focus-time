import numpy as np
from focus.timer_backend import timer

def focus_session(minutes_required = False):
    '''      FOCUS TIMER for one session     '''
    target_focus_duration =         float(input('How long would you like to focus for? (minutes)          '))

    # set the maximum session duration given the target focus time
    if target_focus_duration <= 5: maximum_session_duration = 10.
    elif target_focus_duration <= 15: maximum_session_duration = target_focus_duration * 2
    elif target_focus_duration < 20: maximum_session_duration = 30.
    else: maximum_session_duration = target_focus_duration * 1.5 

    # set the average, minimum and maximum interval between focus reminders (the ding-dong sound)
    if target_focus_duration > 2: average_interval = np.sqrt(target_focus_duration) * 60
    else: average_interval = target_focus_duration / 2 * 60
    minimum_interval = min(20, average_interval/2)
    maximum_interval = average_interval*2

    # Run the session
    time_focused_session = timer(target_focus_duration, maximum_session_duration, average_interval, minimum_interval, maximum_interval, minutes_required)
    return time_focused_session

if __name__ == "__main__":
    focus_session()