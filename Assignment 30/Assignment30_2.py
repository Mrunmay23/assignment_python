def CountWords(fName):
    
    try:
        count = 0
        with open(fName,"r") as fobj:
            for line in fobj:
                words = line.split()
                count = count + len(words)
            
            print(f"Total number of words in {fName} is: ",count)

    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    CountWords(FileName)

if __name__ == "__main__":
    main()