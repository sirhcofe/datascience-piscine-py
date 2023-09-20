import sys

sys.tracebacklimit = 0

length = len(sys.argv)
assert length < 3, "more than one argument is provided"
try:
    input = sys.argv[1]
    int_value = int(input)
    if (int_value % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except IndexError:
    print("IndexError: one argument is required")
except ValueError:
    print("ValueError: argument is not an integer")
