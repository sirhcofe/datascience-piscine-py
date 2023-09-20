def filterstring(array, limit):
    print(ft_filter(lambda x: len(x) > limit, array))


def main():
    """
    Function converts string to list, while omitting illegal words containing
    punctuations or numbers. The list is then parsed for further filtering
    to include only items which size is no more than the number limit defined
    """

    # sys.tracebacklimit determines the maximum number of levels of traceback
    # information printed when unhandled exception occurs (default is 1000)
    sys.tracebacklimit = 0
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        str = sys.argv[1].split()
        num = int(sys.argv[2])
        wordlist = [i for i in str if (i.isalpha())]
        filterstring(wordlist, num)
    except ValueError:
        print("ValueError: 2nd argument must be a number")


if __name__ == "__main__":
    import sys
    from ft_filter import ft_filter
    main()
