import sys

# try-except block to attempt converting a string from 'sys.argv' to an integer
def is_integer(input):
	try:
		int_value = int(input)
		if (int_value % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except ValueError:
		print("AssertionError: argument is not an integer")
		sys.exit(1)

if (len(sys.argv) > 2):
	print("AssertionError: more than one argument is provided")
	sys.exit(1)

input = sys.argv[1]
is_integer(input)
