def focus_session():
    '''      MEDITATION TIMER      '''
    # How long are you meditating for, if you're a good boy? (minutes)
    meditation_time =         float(input('How long would you like to focus for? (minutes)          '))
    #maximum_meditation_time = float(input('How long do you have before life takes over? (minutes)   '))
    if meditation_time <= 5: maximum_meditation_time = 10
    elif meditation_time <= 15: maximum_meditation_time = meditation_time * 2
    elif meditation_time < 20: maximum_meditation_time = 30
    else: maximum_meditation_time = meditation_time * 1.5 

    # How long between each ding dong (seconds)
    #average_interval = float(input('Average inter-ding-dong interval? (seconds)'))
    import numpy as np
    if meditation_time > 2: average_interval = np.sqrt(meditation_time) * 60
    else: average_interval = meditation_time / 2 * 60
    minimum_interval = min(20, average_interval/2) #int(input('Minimum inter-ding-dong interval? (seconds)'))
    maximum_interval = average_interval*2 #int(input('Maximum inter-ding-dong interval? (seconds)'))

    # Run the timer
    from focus.timer_backend import timer
    timer(meditation_time, maximum_meditation_time, average_interval, minimum_interval, maximum_interval)

if __name__ == "__main__":
    focus_session()