import os

def ChkFile(fName):

    if os.path.exists(fName):
        print("File is Present")
    else:
        print("File is Not Present")

def main():
    FileName = input("Enter File name:")
    ChkFile(FileName)

if __name__ == "__main__":
    main()