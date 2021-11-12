from focus.main import Focus

def test_run_timer():
    focus = Focus()
    focus.intended_mins_focus = 0.25
    focus.run_timer()
    assert 0.25 <= focus.mins_focused_in_session < 1.01
    assert not focus.session_failed

def test_report_outcome_of_session():
    # test: just make sure it proceeds without errors 
    focus = Focus()
    focus.report_outcome_of_session('part of a focus day')
    focus.session_failed = True
    focus.report_outcome_of_session('single session')
    focus.session_failed = False
    focus.report_outcome_of_session('single session')

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

# TODO: add mock user input to test this
# def test_session():
#     focus = Focus()
#     focus.session()

# TODO: add mock user input to test this
# def test_day():
#     focus = Focus()
#     focus.day()

# TODO: add mock user input to test this
# def test_query_intended_minutes_focus():
#     focus = Focus()
#     focus.query_intended_minutes_focus

# TODO: add mock user input to test this
# def test_query_intended_hours_of_focus():
#     focus = Focus()
#     focus.query_intended_hours_of_focus()