from focus.main import Focus

def run_focus_session():
    Focus().session() # triggered by entering 'focus', 'focus-time', or 'focus-session' in the terminal

def run_focus_day():
    Focus().day()     # triggered by entering 'focus-day' in the terminal
