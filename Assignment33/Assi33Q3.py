# Add Actual Memory Allocation Feature
# Display real memory usage of each process:
# RSS(Resident Set Size-actual RAM used)
# VMS(Virtual Memory)
# Memory Percentage
# Requirement
# Show :
# Top 10 memory consuming processes.

import psutil
from datetime import datetime

def MemoryMonitoring():

    filename = "MemoryLog.txt"
    process_list = []

    # Collect process memory usage
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            memory_percent = proc.memory_percent()
            process_list.append((proc, memory_percent))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort processes by memory usage (Descending)
    process_list.sort(key=lambda x: x[1], reverse=True)

    top10 = process_list[:10]

    with open(filename, "w") as file:

        file.write("Memory Monitoring Log\n")
        file.write("Timestamp : " + str(datetime.now()) + "\n")
        file.write("-" * 60 + "\n\n")

        for proc, mem in top10:
            try:
                rss = proc.memory_info().rss
                vms = proc.memory_info().vms

                file.write(f"Process Name : {proc.name()}\n")
                file.write(f"PID          : {proc.pid}\n")
                file.write(f"RSS          : {rss}\n")
                file.write(f"VMS          : {vms}\n")
                file.write(f"Memory %     : {mem:.2f}\n")
                file.write("-" * 60 + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    print("Memory Monitoring log created successfully.")


if __name__ == "__main__":
    MemoryMonitoring()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\PlatformSurveillance>python Assi33Q3.py
# Memory Monitoring log created successfully.    