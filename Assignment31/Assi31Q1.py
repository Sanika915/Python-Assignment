# Design automation script which accept directory name and file extenction from user. Display all files with that extenction.
# Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extencsion that we want to search.

import os
import sys

def DirectoryFileSearch(path, ext):
    try:
        if not os.path.isdir(path):
            print("Invalid directory")
            return

        for file in os.listdir(path):
            if file.endswith(ext):
                print(file)

    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py DirectoryName .ext")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi31Q1.py
# Usage: DirectoryFileSearch.py DirectoryName .ext