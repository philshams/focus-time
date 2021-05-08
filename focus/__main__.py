import sys
from focus.session import focus_session


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    focus_session()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do. Return values are exit codes.


if __name__ == "__main__":
    sys.exit(main())