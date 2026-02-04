# Count Lines in a File.
# Problem Statement : Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input : Demo.txt.
# Expected Output : Total number of lines in Demo.txt.

import os

def CountLines(FileName):
    try:
        fobj = open(FileName, "r")
        lines = fobj.readlines()
        fobj.close()

        print("Total number of lines in", FileName, "is:", len(lines))

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():
    name = input("Enter file name: ")
    CountLines(name)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi30Q1.py
# Enter file name: Assi30Q1.py
# Total number of lines in Assi30Q1.py is: 27
# End of Application