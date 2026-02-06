# Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
# Usage : DirectoryDusplicatte.py "Demo"
# Demo is name of directory.

import os
import sys
import hashlib

def hashfile(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(1024):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(dir_name):
    files_hash = {}
    duplicates = []

    for root, _, files in os.walk(dir_name):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hashfile(path)

            if file_hash in files_hash:
                duplicates.append(path)
            else:
                files_hash[file_hash] = path

    return duplicates

def main():
    if len(sys.argv) != 2:
        print("Usage : assi32q2.py <DirectoryName>")
        return

    dup = find_duplicates(sys.argv[1])

    with open("Log.txt", "w") as f:
        for file in dup:
            f.write(file + "\n")

    print("Duplicate files written to Log.txt")

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi32Q2.py Demo
# Duplicate files written to Log.txt