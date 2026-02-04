def Display(fName):

    try:
        fobj = open(fName,"r")
        
        Data = fobj.read()
        print("Data from the File is:")
        print(Data)
        fobj.close()
    except FileNotFoundError:
        print("File is not present.")


def main():
    FileName = input("Enter File name:")
    Display(FileName)

if __name__ == "__main__":
    main()