# Add Periodic Email Reporting Feature
# Automatically send system report through email at regular intervals.
# Email must contain:
# Log file attachment 
# Summary of:
# Total processes
# Top CPU usage processes
# Top Memory usage processes
# Top Thread count processes
# Top Open file processes
# Usage 
# PlatformsSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10
# Where :
# MarvellousLogs -> log folder
# receiver@gamil.com -> receiver mail
# 10 -> interval in minutes

import os
import sys
import time
import psutil
import smtplib
from datetime import datetime
from email.message import EmailMessage

# ---------------------------------------------------------
# Function: Create Log File
# ---------------------------------------------------------
def CreateLog(folder_name):

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder_name, f"Log_{timestamp}.txt")

    with open(filename, "w") as file:

        file.write("System Monitoring Report\n")
        file.write("Timestamp : " + str(datetime.now()) + "\n")
        file.write("-" * 60 + "\n")

        total = len(psutil.pids())
        file.write(f"Total Processes : {total}\n")

        memory = psutil.virtual_memory()
        file.write(f"Total Memory     : {memory.total}\n")
        file.write(f"Available Memory : {memory.available}\n")

        file.write("-" * 60 + "\n")

    return filename

# ---------------------------------------------------------
# Function: Send Email
# ---------------------------------------------------------
def SendEmail(receiver, logfile):

    sender = "your_email@gmail.com"      # Change this
    password = "your_app_password"       # Use Gmail App Password

    msg = EmailMessage()
    msg["Subject"] = "System Monitoring Report"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Please find attached system monitoring report.")

    with open(logfile, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(logfile))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():

    if len(sys.argv) != 4:
        print("Usage: python Assi33Q4.py <FolderName> <ReceiverEmail> <IntervalInMinutes>")
        sys.exit()

    folder = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3]) * 60

    while True:
        logfile = CreateLog(folder)
        SendEmail(receiver, logfile)
        print("Email sent successfully.")
        time.sleep(interval)


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\PlatformSurveillance>python Assi33Q4.py
# Usage: python Assi33Q4.py <FolderName> <ReceiverEmail> <IntervalInMinutes>    