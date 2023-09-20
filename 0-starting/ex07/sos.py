def encode_to_morse(text):
    """
    Function creates a dictionary of alphanumeric and its morse code
    equivalent. The dictionary is then compared with every character of the
    text string, and convert them to morse code

        Parameters:
            test: The text to convert to morse code
        Return:
            The morse code translation of the text
    """

    # Added whitespace behind to ease combining characters in morse code
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    morse_code = ""
    for c in text.upper():
        if c in NESTED_MORSE:
            morse_code += NESTED_MORSE[c]
        else:
            raise AssertionError("the arguments are bad")
    return morse_code


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are badd")
    input = sys.argv[1]
    morse_code = encode_to_morse(input)
    print(morse_code)


if __name__ == "__main__":
    import sys
    sys.tracebacklimit = 0
    main()
