# Write a python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Value1 and Value2.
# Define a constructor(__init__) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept() - accepts values for Value1 and Value2 from the user.
# Addition() - returns the addition of Value1 and Value2.
# Subtraction() - returns the subtraction of Value1 and Value2.
# Multiplication() - returns the multiplication of Value1 and Value2.
# Division() - returns the division of Value1 and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value : "))
        self.Value2 = int(input("Enter second value : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not possible"
        else:
            return self.Value1 / self.Value2

def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj1.Accept()
    print("Addition =", obj1.Addition())
    print("Subtraction =", obj1.Subtraction())
    print("Multiplication =", obj1.Multiplication())
    print("Division =", obj1.Division())

    obj2.Accept()
    print("Addition =", obj2.Addition())
    print("Subtraction =", obj2.Subtraction())
    print("Multiplication =", obj2.Multiplication())
    print("Division =", obj2.Division())

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi22Q3.py
# Enter first value : 5
# Enter second value : 3
# Addition = 8
# Subtraction = 2
# Multiplication = 15
# Division = 1.6666666666666667

# Enter first value : 9
# Enter second value : 3
# Addition = 12
# Subtraction = 6
# Multiplication = 27
# Division = 3.0