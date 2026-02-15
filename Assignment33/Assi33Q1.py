# Add Thread Monitoring Feature
# For each running process,display :
# Process Name
# PID
# Number of Threads created by that process
# Requirement
# Store information in log file along with timestamp.

import psutil
from datetime import datetime

# Function to get thread information
def ThreadMonitoring():

    print("Thread Monitoring Information")
    print("-" * 50)

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            threads = proc.num_threads()

            print("Process Name :", name)
            print("PID          :", pid)
            print("Thread Count :", threads)
            print("Timestamp    :", datetime.now())
            print("-" * 50)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    ThreadMonitoring()