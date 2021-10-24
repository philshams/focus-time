from focus.timer import Timer

def test_Timer():
    intended_mins_of_focus = 60
    timer = Timer(intended_mins_of_focus)

    assert timer.intended_mins_of_focus == 60