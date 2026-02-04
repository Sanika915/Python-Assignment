# Check File Exists in Current Directory.
# Problem Stament: Write a program accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input : Demo.txt
# Expected Output : Display whether Demo.txt exists or not.

import os

def main():
    filename = input("Enter file name: ")

    current_path = os.getcwd()
    full_path = os.path.join(current_path, filename)

    if os.path.exists(full_path):
        print(f"File '{filename}' exists at path:")
        print(full_path)
    else:
        print(f"File '{filename}' does not exist in path:")
        print(current_path)

if __name__ == "__main__":
    main()

# Output is:
# Enter file name: Demo.txt
# File 'Demo.txt' does not exist in path:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment
