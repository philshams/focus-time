from focus.timer import Timer
from focus.main import Focus

def test_start_sound():
    focus = Focus()
    timer = Timer(60)
    if focus.sound:
        timer.initiate_session(sound=True)

def test_reminder_sound():
    focus = Focus()
    timer = Timer(60)
    if focus.sound:
        timer.sound = True
        timer.inter_reminder_interval = 21
        timer.mins_focused_so_far = 0
        timer.issue_reminder()

def test_session_outcome_sounds():
    focus = Focus()
    for failure in [True,False]:
        for context in ['single session', 'part of a focus day']:
            focus.session_failed = failure
            if focus.sound: focus.report_outcome_of_session(context)

def test_day_complete_sound():
    focus = Focus()
    if focus.sound:
        focus.report_outcome_of_day()       
