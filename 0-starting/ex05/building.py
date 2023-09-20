def building(str):
    characters = len(str)
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper = sum(1 for c in str if c.isupper())
    lower = sum(1 for c in str if c.islower())
    punctuation = sum(1 for c in str if c in punc)
    space = sum(1 for c in str if c.isspace())
    digit = sum(1 for c in str if c.isdigit())
    print(f"The text contains {characters} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    try:
        length = len(sys.argv)
        if (length > 2):
            raise AssertionError("more than one argument is provided")
        elif (length < 2):
            str = input("What is the text to count?\n")
        else:
            str = sys.argv[1]
        building(str)
    except EOFError:
        print()
    except KeyboardInterrupt:
        print()


"""
The following line is a common Python programming construct used to determine
whether the Python script is being run as the main program or it is being
imported as a module into another script
"""
if __name__ == "__main__":
    import sys
    sys.tracebacklimit = 0
    main()
