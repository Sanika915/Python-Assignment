# Copy File Contenst into a New File(Command Line)
# Problem Statemet : Write a program which accepts an existing file name through command line arguments, cresates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line) : ABC.txt
# Expected Output : Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide file name through command line")
        return

    source_file = sys.argv[1]
    current_path = os.getcwd()

    source_path = os.path.join(current_path, source_file)
    destination_path = os.path.join(current_path, "Demo.txt")

    if os.path.exists(source_path):
        src = open(source_path, "r")
        dest = open(destination_path, "w")

        dest.write(src.read())

        src.close()
        dest.close()

        print("File copied successfully")
        print("Source file path:")
        print(source_path)
        print("Destination file path:")
        print(destination_path)
    else:
        print("Source file does not exist at path:")
        print(current_path)

if __name__ == "__main__":
    main()

# Output is: