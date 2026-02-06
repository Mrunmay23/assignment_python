
import sys
import os
import time
import hashlib

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName, "rb")
        hobj = hashlib.md5()

        Buffer = fobj.read(1024)
        while Buffer:
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()
        return hobj.hexdigest()

    except Exception:
        return "Error while calculating checksum"

# -------------------------------------------------
# Function to create log file
# -------------------------------------------------
def CreateLogFile():
    timestamp = time.ctime()
    LogFileName = "DirectoryChecksumLog_%s.log" % timestamp

    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    fobj = open(LogFileName, "a")
    fobj.write("------------------------------------\n")
    fobj.write("Log file created at : " + time.ctime() + "\n")
    fobj.write("------------------------------------\n")

    return fobj

# -------------------------------------------------
# Function to validate directory
# -------------------------------------------------
def ValidateDirectory(DirName, fobj):
    if not os.path.exists(DirName):
        fobj.write("ERROR : Directory does not exist\n")
        return False

    if not os.path.isdir(DirName):
        fobj.write("ERROR : Given path is not a directory\n")
        return False

    return True

# -------------------------------------------------
# Function to display checksum of files
# -------------------------------------------------
def DisplayChecksum(DirName, fobj):
    count = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for file in FileNames:
            FilePath = os.path.join(FolderName, file)
            checksum = CalculateChecksum(FilePath)

            fobj.write(FilePath + " --> Checksum : " + checksum + "\n")
            count += 1

    fobj.write("\nTotal files processed : " + str(count) + "\n")

# -------------------------------------------------
# Main function
# -------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print("Usage : python3 Assignment31_1.py <DirectoryName>")
        return

    DirName = sys.argv[1]

    try:
        fobj = CreateLogFile()

        if ValidateDirectory(DirName, fobj):
            DisplayChecksum(DirName, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error occurred :", e)

# -------------------------------------------------
# Starter
# -------------------------------------------------
if __name__ == "__main__":
    main()
