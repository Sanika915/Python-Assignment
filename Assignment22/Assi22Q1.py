# Write a Python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables : no1 and no2.
# The class should contain one class variable named Value.
# Define a constructor(__init__) that accepts two parameters and initialize the instance variables.
# Implement two instance methods:
# Fun() - display the values of instance variables no1 and no2.
# Gun() - display the values of instance variables no1 and no2.
# Create two objects of the Demo class as follows:
# obj1 = Demo(11,21)
# obj2 = Demo(51,101)
# Call the instance methods in the given sequence:
# obj1.Fun()
# obj2.Gun()
# obj2.Gun()

class Demo:
    Value = 0   # Class variable

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("no1 =", self.no1)
        print("no2 =", self.no2)

    def Gun(self):
        print("no1 =", self.no1)
        print("no2 =", self.no2)


def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi22Q1.py
# no1 = 11
# no2 = 21
# no1 = 51
# no2 = 101
# no1 = 51
# no2 = 101