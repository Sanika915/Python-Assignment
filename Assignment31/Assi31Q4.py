# Design automation script which accept two directory names and one file extencsion. Copy all files with the specified extencsion from first directory into second directory. Second directory should be created at run time.
# Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains file in it. We havte to create new Directory as Temp and copy all files with extenction .exe from Demo to Temp.

import os
import sys
import shutil

def DirectoryCopyExt(src, dest, ext):
    try:
        if not os.path.isdir(src):
            print("Invalid source directory")
            return

        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            if file.endswith(ext):
                src_path = os.path.join(src, file)
                dest_path = os.path.join(dest, file)
                shutil.copy(src_path, dest_path)

    except Exception as e:
        print("Error :", e)

def main():
    if len(sys.argv) != 4:
        print("Usage: assi31q4.py SrcDir DestDir .ext")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi31Q4.py
# Usage: assi31q4.py SrcDir DestDir .ext    