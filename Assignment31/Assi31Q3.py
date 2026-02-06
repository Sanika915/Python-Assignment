# Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.

import os
import sys
import shutil

def DirectoryCopy(src, dest):
    try:
        if not os.path.isdir(src):
            print("Invalid source directory")
            return

        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            src_path = os.path.join(src, file)
            dest_path = os.path.join(dest, file)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)

    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: assi31q3.py SourceDir DestinationDir")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi31Q3.py
# Usage: assi31q3.py SourceDir DestinationDir