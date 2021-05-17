import sys
from focus.day import focus_day


def day(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    focus_day()

if __name__ == "__main__":
    sys.exit(day())