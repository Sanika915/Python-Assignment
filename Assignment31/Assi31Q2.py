# Design automation script which accept directory name and two file extensions from user. Rename all files with first file extencsion with the second file extenction.
# Usage : DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is anme of directory and .txt is the extenction that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os
import sys

def DirectoryRename(path, old_ext, new_ext):
    try:
        if not os.path.isdir(path):
            print("Invalid directory")
            return

        for file in os.listdir(path):
            if file.endswith(old_ext):
                old_path = os.path.join(path, file)
                new_file = file.replace(old_ext, new_ext)
                new_path = os.path.join(path, new_file)
                os.rename(old_path, new_path)

    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 4:
        print("Usage: Assi31Q2.py DirectoryName .old_ext .new_ext")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi31Q2.py
# Usage: Assi31Q2.py DirectoryName .old_ext .new_ext