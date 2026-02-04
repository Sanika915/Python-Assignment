# Comapre Two Files(Command Line).
# Problem Statemt : Write a program which accepts two file names through command line arguments and compares the contents of both files.
# If both files contain the same contents, disply Success.
# Otherwise display Failure.
# Input (Command Line): Demo.txt Hello.txt
# Expected Output: Success OR Failure.

import os
import sys

def CompareFiles(file1, file2):
    current_path = os.getcwd()
    path1 = os.path.join(current_path, file1)
    path2 = os.path.join(current_path, file2)

    if not os.path.exists(path1) or not os.path.exists(path2):
        print("One or both files do not exist")
        return

    f1 = open(path1, "r")
    f2 = open(path2, "r")

    if f1.read() == f2.read():
        print("Success")
    else:
        print("Failure")

    f1.close()
    f2.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python Assi29Q4.py Demo.txt Hello.txt")
        return

    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi29Q4.py
# Usage: python Assi29Q4.py Demo.txt Hello.txt