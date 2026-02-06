import sys
import os
import time
import shutil

# Function to create log file
def CreateLog():
    timestamp = time.ctime()
    LogFile = "DirectoryCopyLog_%s.log" % timestamp

    LogFile = LogFile.replace(" ", "_")
    LogFile = LogFile.replace(":", "_")

    fobj = open(LogFile, "a")
    fobj.write("\n----------------------------------\n")
    fobj.write("Log created at : " + time.ctime() + "\n")

    return fobj


# Function to validate source directory
def ValidateSourceDirectory(dirname, fobj):

    if not os.path.exists(dirname):
        fobj.write("ERROR : Source directory does not exist\n")
        return False

    if not os.path.isdir(dirname):
        fobj.write("ERROR : Source path is not a directory\n")
        return False

    return True


# Function to create destination directory
def CreateDestinationDirectory(dirname, fobj):

    if not os.path.exists(dirname):
        os.mkdir(dirname)
        fobj.write("Destination directory created : " + dirname + "\n")
    else:
        fobj.write("Destination directory already exists\n")


# Function to copy files
def CopyFiles(src, dest, fobj):

    count = 0

    for folder, subfolder, files in os.walk(src):
        for fname in files:
            src_path = os.path.join(folder, fname)
            dest_path = os.path.join(dest, fname)

            shutil.copy2(src_path, dest_path)
            fobj.write(f"Copied : {src_path} --> {dest_path}\n")
            count += 1

    fobj.write("Total files copied : " + str(count) + "\n")


# Main function
def main():

    if len(sys.argv) != 3:
        print("Usage : DirectoryCopy.py <SourceDirectory> <DestinationDirectory>")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    try:
        fobj = CreateLog()

        if ValidateSourceDirectory(src_dir, fobj):
            CreateDestinationDirectory(dest_dir, fobj)
            CopyFiles(src_dir, dest_dir, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error :", e)



if __name__ == "__main__":
    main()
