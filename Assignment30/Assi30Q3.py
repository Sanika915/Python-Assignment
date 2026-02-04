# Display File Line by Line.
# Problem Statemt : Write a program which accepts a file name from the user and displays  the contents of the file line by line on the screen.
# Input : Demo.txt
# Expected Output: Display each line Demo.txt one by one.

import os

def DisplayFileLineByLine(FileName):
    try:
        with open(FileName, "r") as fobj:
            print("\nContents of file are (line by line):\n")
            for line in fobj:
                print(line, end="")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

def main():
    Name = input("Enter File Name: ")
    DisplayFileLineByLine(Name)

if __name__ == "__main__":
    main()

# Output is: