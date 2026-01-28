# Write a Python program to implement a class named BookStore with the following specifications:
# The class should contain two instance variables:
# Name(Book Name)
# Author(Book Author)
# The class should contain one class variable.
# NoOfBooks(initialize it to 0)
# Define a constructor(__init__) that accepts Name and Author and initializes instance variables.
# Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
# Implement an instance method:
# Display() - should display book details in the format:
# <BOOKName> by <Author>, No of books: <NoOfBooks>
# Example usage:
# obj1 = BookStore("Linux System Programming","Robert Love")
# obj1.Display() # Linux sysytem programming by Robert Love. No of books : 1
# obj2 = BookStore("C programming","Dennis Ritche")
# obj2.Display() # C Programming by Dennis Ritchie. No of Books: 2

class BookStore:
    NoOfBooks = 0 
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1 

    def Display(self):
        print(f"{self.Name} by {self.Author}, No of books: {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()  

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()  

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi23Q1.py
# Linux System Programming by Robert Love, No of books: 1
# C Programming by Dennis Ritchie, No of books: 2