def CountLines(fName):
    
    try:
        count = 0
        with open(fName,"r") as fobj:
            for line in fobj:
                count = count + 1
        print("Total no of lines are: ",count)
    
    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    CountLines(FileName)

if __name__ == "__main__":
    main()