import sys
import os
import time

# Function to create log file
def CreateLog():
    timestamp = time.ctime()
    LogFile = "DirectoryRenameLog_%s.log" % timestamp

    LogFile = LogFile.replace(" ", "_")
    LogFile = LogFile.replace(":", "_")

    fobj = open(LogFile, "a")
    fobj.write("\n----------------------------------\n")
    fobj.write("Log created at : " + time.ctime() + "\n")

    return fobj


# Function to validate directory
def ValidateDirectory(dirname, fobj):

    if not os.path.exists(dirname):
        fobj.write("ERROR : Directory does not exist\n")
        return False

    if not os.path.isdir(dirname):
        fobj.write("ERROR : Given path is not a directory\n")
        return False

    return True


# Function to rename files
def RenameFiles(dirname, old_ext, new_ext, fobj):

    count = 0

    for folder, subfolder, files in os.walk(dirname):
        for fname in files:
            name, ext = os.path.splitext(fname)

            if ext == old_ext:
                old_path = os.path.join(folder, fname)
                new_name = name + new_ext
                new_path = os.path.join(folder, new_name)

                os.rename(old_path, new_path)
                fobj.write(f"Renamed : {old_path} --> {new_path}\n")
                count += 1

    fobj.write("Total files renamed : " + str(count) + "\n")


# Main function
def main():

    if len(sys.argv) != 4:
        print("Usage : DirectoryRename.py <DirectoryName> <OldExtension> <NewExtension>")
        return

    dirname = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname, fobj):
            RenameFiles(dirname, old_ext, new_ext, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error :", e)


# Entry point
if __name__ == "__main__":
    main()
