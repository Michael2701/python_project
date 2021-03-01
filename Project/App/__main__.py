import sys
from App.Controllers.Gui import Gui

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    Gui()


if __name__ == "__main__":
    sys.exit(main())