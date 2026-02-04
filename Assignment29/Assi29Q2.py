# Display File Contents
# problem Stament: Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input : Demo.txt
# Expected Output : Displays contents of Demo.txt on consol.

import os

def main():
    filename = input("Enter file name: ")

    current_path = os.getcwd()
    full_path = os.path.join(current_path, filename)

    if os.path.exists(full_path):
        print(f"File opened from path:")
        print(full_path)
        print("\n----- File Contents -----\n")

        fileobj = open(full_path, "r")
        print(fileobj.read())
        fileobj.close()
    else:
        print("File does not exist at path:")
        print(current_path)

if __name__ == "__main__":
    main()

# Output is:
# Enter file name: Demo.txt
# File does not exist at path:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment