# Frequency of a String in File.
# Problem Statement: Write a program which accepts a file name and one string from the user and returns the frequency(count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# Expected Output : Count how many time "Marvellous" appears in Demo.txt.

import os

def main():
    filename = input("Enter file name: ")
    search_string = input("Enter string to search: ")

    if not os.path.exists(filename):
        print("File does not exist")
        return

    fileobj = open(filename, "r")
    data = fileobj.read()
    fileobj.close()

    count = data.count(search_string)

    print(f'Frequency of "{search_string}" in {filename} is: {count}')

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi29Q5.py
# Enter file name: Demo.txt Marvellous
# Enter string to search: 1
# File does not exist