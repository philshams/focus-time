from focus.timer import Timer
from focus.main import Focus
from playsound import playsound

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
    if focus.sound:
        focus.session_failed = True
        focus.report_outcome_of_session('single session')
        focus.session_failed = False
        focus.report_outcome_of_session('single session')

def test_day_complete_sound():
    focus = Focus()
    if focus.sound:
        focus.report_outcome_of_day()       
