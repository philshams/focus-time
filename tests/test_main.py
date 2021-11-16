from focus.main import Focus
from io import StringIO
import sys

def test_run_timer():
    focus = Focus()
    focus.intended_mins_focus = 0.25
    focus.run_timer()
    assert 0.25 <= focus.mins_focused_in_session < 1.25
    assert not focus.session_failed

def test_query_intended_minutes_focus():
    # test: just make sure it proceeds without errors 
    focus = Focus()
    sys.stdin = StringIO('60\n') 
    focus.query_intended_minutes_focus()
    assert focus.intended_mins_focus == 60

def test_query_intended_hours_of_focus():
    focus = Focus()
    sys.stdin = StringIO('8\n')
    focus.query_intended_hours_of_focus()
    assert focus.intended_hours_of_focus == 8

def test_report_outcome_of_session():
    # test: just make sure it proceeds without errors 
    focus = Focus()
    for failure in [True,False]:
        for context in ['single session', 'part of a focus day']:
            focus.session_failed = failure
            if focus.sound: focus.report_outcome_of_session(context)

def test_report_hours_of_focus_remaining():
    focus = Focus()
    focus.intended_hours_of_focus = 3
    focus.hours_of_focus = 1
    focus.session_num = 0
    focus.report_hours_of_focus_remaining()
    assert focus.hours_of_focus_left == 2
    assert focus.session_num == 1

def test_report_outcome_of_day():
    # test: just make sure it proceeds without errors 
    focus = Focus()
    focus.report_outcome_of_day

def test_test_speaker():
    # test: just make sure it proceeds without errors 
    # since function output will depend on which device is used
    focus = Focus()
    focus.test_speakers()

