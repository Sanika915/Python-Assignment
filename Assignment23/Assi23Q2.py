# Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables.
# Name(Account holder name)
# Amount(Account balance)
# The class should contain one class variable.
# ROI(Rate of Interest), initialized to 10.5
# Define a constructor(__init__)that accepts Name and initial Amount.
# Implement the following instance methods:
# Display() - displays account holder name and current balance
# Deposit() - accepts an amount from the user and adds it to balance.
# Withdraw() - accepts an amount from the user and subtracts it from balance(Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest() - calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5  

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}, Current Balance: {self.Amount}")

    def Deposit(self):
        amt = float(input(f"Enter amount to deposit for {self.Name}: "))
        self.Amount += amt
        print(f"Amount deposited. New Balance: {self.Amount}")

    def Withdraw(self):
        amt = float(input(f"Enter amount to withdraw for {self.Name}: "))
        if amt > self.Amount:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.Amount -= amt
            print(f"Amount withdrawn. New Balance: {self.Amount}")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest for {self.Name} at ROI {BankAccount.ROI}%: {interest}")
        return interest

def main():
    acc1 = BankAccount("Alice", 5000)
    acc2 = BankAccount("Bob", 10000)

    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()

    print()
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi23Q2.py
# Account Holder: Alice, Current Balance: 5000
# Enter amount to deposit for Alice: 3456
# Amount deposited. New Balance: 8456.0
# Enter amount to withdraw for Alice: 235
# Amount withdrawn. New Balance: 8221.0
# Interest for Alice at ROI 10.5%: 863.205

# Account Holder: Bob, Current Balance: 10000
# Enter amount to deposit for Bob: 78
# Amount deposited. New Balance: 10078.0
# Enter amount to withdraw for Bob: 1234
# Amount withdrawn. New Balance: 8844.0
# Interest for Bob at ROI 10.5%: 928.62