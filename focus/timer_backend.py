import numpy as np
import time
from playsound import playsound
import msvcrt
from datetime import datetime
from pathlib import Path

def focus_query(caption, timeout = 5):
    start_time = time.time()
    while msvcrt.kbhit(): msvcrt.getche() # Remove keys pressed in the interval
    print(caption);
    playsound(str(Path(__file__).parent / '../data/ding dong.mp3'))
    while True: # If a key is pressed, return False; otherwise True
        if msvcrt.kbhit(): return False
        if (time.time() - start_time) > timeout: return True


def timer(meditation_time, maximum_meditation_time, average_interval, minimum_interval, maximum_interval):  
    print(datetime.now())
    print('\nstarting focus session for ' + str(meditation_time) + ' to ' + str(maximum_meditation_time) + ' minutes\n')
    playsound(str(Path(__file__).parent / '../data/start.mp3'))
    # how much time is left
    meditation_time_left = meditation_time*60
    # set a timer for the whole session
    start_time = time.time()
    time_elapsed = 0
    failed = False
    # Start the main loop
    while meditation_time_left > 0:
        # Select the interval
        interval = -1
#        print(minimum_interval)
#        print(maximum_interval)
        while interval < minimum_interval or interval > maximum_interval:
            interval = np.random.exponential(scale = (average_interval - minimum_interval)) + minimum_interval
        # Wait for the interval
#        print(datetime.now())
#        print(np.round(interval/60))
        seconds_of_interval = 0
        while seconds_of_interval < interval:
            time.sleep(1)
            time_elapsed = time.time() - start_time
            if int(time_elapsed) % 60 == 0: print('')
            if time_elapsed > maximum_meditation_time*60:
                print('Out of time.')
                playsound(str(Path(__file__).parent / '../data/failure.mp3'))
                failed = True
                break
            seconds_of_interval += 1

        
        if failed: break
        # Were you focusing?   
        ans = focus_query('Were you focusing? If yes, carry on. If no, press any key within 10 seconds', timeout = 10) 
        if ans:
            print('\nGreat job!')
            meditation_time_left -= (interval+10)
            print(str(np.round(100-100*meditation_time_left / (meditation_time*60))) + '% done\n')
        else:
            print('Keep at it, champ\n')
    if not failed:
        print('You did it!!!')
        playsound(str(Path(__file__).parent / '../data/success.mp3'))
    
