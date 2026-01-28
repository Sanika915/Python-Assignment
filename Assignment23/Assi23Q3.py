# Write a python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor(__init__) that accepts a number from the user and initializes value.
# Implement the following instance methods:
# ChkPrime() - returns True if the number is prime,otherwise returns False
# ChkPerfect() - returns True if the number is perfect, otherwise return False
# Factors() - displays all factors of the number
# SumFactors() - returns the sum of all factors(You may uses this method as a helper in CHKPerfect() if required)
# Create multiple objects and call all methods.

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        factors = [i for i in range(1, self.Value + 1) if self.Value % i == 0]
        print(f"Factors of {self.Value}:", factors)
        return factors

    def SumFactors(self):
        factors = self.Factors()
        sum_factors = sum(factors)
        return sum_factors

    def ChkPerfect(self):
        proper_factors = [i for i in range(1, self.Value) if self.Value % i == 0]
        return sum(proper_factors) == self.Value

def main():
    num1 = Numbers()
    print("Is Prime", num1.ChkPrime())
    print("Is Perfect", num1.ChkPerfect())
    num1.Factors()
    print("Sum of factors:", num1.SumFactors())

    print()  

    num2 = Numbers()
    print("Is Prime", num2.ChkPrime())
    print("Is Perfect", num2.ChkPerfect())
    num2.Factors()
    print("Sum of factors:", num2.SumFactors())

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi23Q3.py
# Enter a number: 6
# Is Prime False
# Is Perfect True
# Factors of 6: [1, 2, 3, 6]
# Factors of 6: [1, 2, 3, 6]
# Sum of factors: 12

# Enter a number: 7
# Is Prime True
# Is Perfect False
# Factors of 7: [1, 7]
# Factors of 7: [1, 7]
# Sum of factors: 8