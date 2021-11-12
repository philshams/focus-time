from focus.timer import Timer
import time 
import numpy as np

def test_init():
    timer = Timer(60)
    assert timer.intended_mins_of_focus == 60

def test_time_session():
    timer = Timer(60)
    pass

def test_calculate_max_session_duration():
    test_input =     [0, 1, 14, 18, 60, 180]
    desired_output = [10,10,28, 30, 90, 270]
    for intended_mins, max_mins in zip(test_input, desired_output):
        timer = Timer(intended_mins)
        timer.calculate_max_session_duration()
        assert timer.max_mins_in_session == max_mins

def test_calculate_inter_reminder_interval_parameters():
    test_input = [0, 1, 18,  60, 180]
    avg_output = [30,30,254,464, 804]
    min_output = [15,15,20, 20,  20 ]
    max_output = [60,60,508,928, 1608]
    for intended_mins, avg, min_, max_ in zip(test_input, avg_output, min_output, max_output):
        timer = Timer(intended_mins)
        timer.calculate_max_session_duration()
        assert timer.avg_inter_reminder_interval == avg
        assert timer.min_inter_reminder_interval == min_
        assert timer.max_inter_reminder_interval == max_

def test_initiate_session():
    timer = Timer(60).initiate_session()
    assert True # just make sure it proceeds without errors

def test_select_inter_reminder_interval():
    timer = Timer(60)
    timer.select_inter_reminder_interval()
    assert 20 <= timer.inter_reminder_interval <= 928

def test_wait_until_next_reminder():
    timer = Timer(60)
    timer.inter_reminder_interval = 21
    timer.session_start_time = time.time()
    timer.wait_until_next_reminder()
    assert int(time.time() - timer.session_start_time) == 21
    assert np.round(timer.mins_elapsed_in_session*60) == 21

def test_time_is_up() -> bool:
    timer = Timer(60)
    pass      

def test_issue_reminder():
    timer = Timer(60)
    pass

def test_user_says_theyre_focused():
    timer = Timer(60)
    pass

def test_key_pressed():
    timer = Timer(60)
    pass

def test_disregard_keys_pressed_during_inter_reminder_interval():
    timer = Timer(60)
    pass