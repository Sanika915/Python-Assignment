# Add Open Files Monitoring Feature
# For each process,display:
# Number of files opened by the process
# Requirement
# Count open file descriptors using system/library calls
# Handle permission errors properly
# Mention "Access Denied" in log if required

import psutil
from datetime import datetime

def OpenFileMonitoring():

    filename = "OpenFileLog.txt"

    with open(filename, "w") as file:

        file.write("Open File Monitoring Log\n")
        file.write("Timestamp : " + str(datetime.now()) + "\n")
        file.write("-" * 60 + "\n\n")

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']

                try:
                    open_files = len(proc.open_files())
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    open_files = "Access Denied"

                file.write(f"Process Name : {name}\n")
                file.write(f"PID          : {pid}\n")
                file.write(f"Open Files   : {open_files}\n")
                file.write("-" * 60 + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    print("Open File Monitoring log created successfully.")

if __name__ == "__main__":
    OpenFileMonitoring()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\PlatformSurveillance>python Assi33Q2.py
# Open File Monitoring log created successfully.    