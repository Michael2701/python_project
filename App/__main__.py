""" This file is entry point to the App. """

import sys
from App.Index import Index


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    Index()


if __name__ == "__main__":
    sys.exit(main())
