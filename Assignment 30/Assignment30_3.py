def DisplayLine(fName):
    
    try:
        with open(fName,"r") as fobj:
            for line in fobj:
                print(line)
               

    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    DisplayLine(FileName)

if __name__ == "__main__":
    main()