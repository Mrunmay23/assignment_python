def CountFrequency(fname, word):

    try:
        with open(fname, "r") as fobj:
            data = fobj.read()

            count = data.count(word)

            print("Frequency is:", count)

    except FileNotFoundError:
        print("File not found")


def main():
    filename = input("Enter file name: ")
    string = input("Enter string to search: ")

    CountFrequency(filename, string)


if __name__ == "__main__":
    main()