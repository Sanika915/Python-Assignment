#  Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py "Demo"
# Demo is name of directory.

import os
import sys
import hashlib

def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def directory_checksum(dir_name):
    if not os.path.isdir(dir_name):
        print("Invalid directory name")
        return

    for file in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file)
        if os.path.isfile(file_path):
            checksum = calculate_checksum(file_path)
            print(f"{file} : {checksum}")

def main():
    if len(sys.argv) != 2:
        print("Usage : assi32q1.py <DirectoryName>")
        return

    directory_checksum(sys.argv[1])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi32Q1.py Demo
# a.txt : d41d8cd98f00b204e9800998ecf8427e
# a_copy.txt : d41d8cd98f00b204e9800998ecf8427e
# b.txt : d41d8cd98f00b204e9800998ecf8427e