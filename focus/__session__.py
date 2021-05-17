import sys
from focus.session import focus_session


def session(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    focus_session()

if __name__ == "__main__":
    sys.exit(session())