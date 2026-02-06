# Design automation script which accept directory name and delete all duplicate files from that directory.Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
# Usage : DirectoryDusplicateRemoval.py "Demo"
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

def delete_duplicates(dir_name):
    files_hash = {}
    deleted = []

    for root, _, files in os.walk(dir_name):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hashfile(path)

            if file_hash in files_hash:
                os.remove(path)
                deleted.append(path)
            else:
                files_hash[file_hash] = path

    return deleted

def main():
    if len(sys.argv) != 2:
        print("Usage : assi32q3.py <DirectoryName>")
        return

    deleted_files = delete_duplicates(sys.argv[1])

    with open("Log.txt", "w") as f:
        for file in deleted_files:
            f.write(file + "\n")

    print("Duplicate files deleted and logged")

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi32Q3.py Demo
# Duplicate files deleted and logged    