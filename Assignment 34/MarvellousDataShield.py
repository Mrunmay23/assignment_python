import os
import sys
import time
import zipfile
import smtplib
from email.message import EmailMessage


def Send_Mail(sender, app_password, receiver, subject, body, attachment):

    try:
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.set_content(body)

        with open(attachment, "rb") as f:
            file_data = f.read()

        msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=os.path.basename(attachment))

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        smtp.quit()

    except Exception as e:
        print("Unable to send mail :", e)


def CreateLogFolder():

    if not os.path.exists("Logs"):
        os.mkdir("Logs")
        print("Logs folder created successfully")


def UpdateHistory(date, count, size):

    try:
        with open("BackupHistory.txt", "a") as f:
            f.write(date + " | Files : " + str(count) +
                    " | Size : " + str(size) + " MB\n")
    except:
        pass

def BackupDirectory(source, email):

    Border = "-" * 50

    if not os.path.exists(source):
        print("Directory does not exist")
        return

    if not os.path.isdir(source):
        print("Given path is not directory")
        return

    CreateLogFolder()

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    zipname = "Backup_%s.zip" % timestamp
    zippath = os.path.join("Logs", zipname)

    count = 0
    exclude = [".tmp", ".log", ".exe"]

    try:
        zipf = zipfile.ZipFile(zippath, 'w')

        for FolderName, SubFolders, FileNames in os.walk(source):

            for file in FileNames:

                if file.endswith(tuple(exclude)):
                    continue

                FullPath = os.path.join(FolderName, file)
                zipf.write(FullPath)
                count = count + 1

        zipf.close()

        size = round(os.path.getsize(zippath) / (1024 * 1024), 2)

        logfile = os.path.join("Logs", "Log_%s.txt" % timestamp)

        fobj = open(logfile, "w")

        fobj.write(Border + "\n")
        fobj.write("Marvellous Data Shield System\n")
        fobj.write("Backup Time : " + time.ctime() + "\n")
        fobj.write("Files Copied : " + str(count) + "\n")
        fobj.write("Zip Name : " + zipname + "\n")
        fobj.write(Border + "\n")

        fobj.close()

        UpdateHistory(time.ctime(), count, size)

        # Mail Details
        sender = "abc798300@gmail.com"
        app_password = "tekq rshb acnv ysus"

        subject = "Backup Completed"
        body = "Backup completed successfully.\nTotal Files : %s" % count

        Send_Mail(sender, app_password, email, subject, body, logfile)

        print("Backup Completed Successfully")

    except Exception as e:
        print("Error during backup :", e)


def RestoreBackup(zipfile_name, destination):

    if not os.path.exists(zipfile_name):
        print("Zip file not found")
        return

    if not os.path.exists(destination):
        os.mkdir(destination)

    try:
        zipf = zipfile.ZipFile(zipfile_name, 'r')
        zipf.extractall(destination)
        zipf.close()

        print("Restore Completed Successfully")

    except Exception as e:
        print("Error during restore :", e)


def ShowHistory():

    if not os.path.exists("BackupHistory.txt"):
        print("No history available")
        return

    fobj = open("BackupHistory.txt", "r")
    data = fobj.read()
    print(data)
    fobj.close()

def main():

    Border = "-" * 50

    print(Border)
    print("---- Marvellous Data Shield System -----")
    print(Border)

    if(len(sys.argv) == 4 and sys.argv[1] == "--backup"):

        source = sys.argv[2]
        email = sys.argv[3]

        BackupDirectory(source, email)

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):

        zipfile_name = sys.argv[2]
        destination = sys.argv[3]

        RestoreBackup(zipfile_name, destination)

    elif(len(sys.argv) == 2 and sys.argv[1] == "--history"):

        ShowHistory()

    else:
        print("Invalid arguments")
        print("Use following options:")
        print("Backup  : python Script.py --backup SourceDir Email")
        print("Restore : python Script.py --restore ZipFile Destination")
        print("History : python Script.py --history")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()
