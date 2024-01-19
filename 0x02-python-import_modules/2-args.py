#!/usr/bin/python3

import sys


def print_arguments(argv):
    num_args = len(argv)

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 0:
        print(".")
    else:
        print("s:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments(sys.argv[1:])


