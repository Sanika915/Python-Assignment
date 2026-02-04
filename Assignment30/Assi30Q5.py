# Search a Word in File.
# Probelm Statement : Write a program which accepts a file names and a word from the user and checks whether that word is present in the file or not.
# Input : Demo.txt Marvellous
# Expected Output: Display whether the word Marvellous is found in Demo.txt or not.

def SearchWord(FileName, Word):
    try:
        fobj = open(FileName, "r")
        data = fobj.read()
        fobj.close()

        if Word in data:
            print("Word", Word, "is found in", FileName)
        else:
            print("Word", Word, "is not found in", FileName)

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():
    name = input("Enter file name: ")
    word = input("Enter word to search: ")

    SearchWord(name, word)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi30Q5.py
# Enter file name: Demo.txt
# Enter word to search: Marvellous
#Word Marvellous is found in Demo.txt