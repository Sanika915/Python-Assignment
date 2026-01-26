# Write a program which accept one number and display below pattern.
# Input : 5 
# Output: * * * * * 
#         * * * *
#         * * * 
#         * * 
#         *    

def Display(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter Number : "))
    Display(Value)

if __name__ == "__main__":
    main()
   
# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi17Q6.py
# Enter Number : 5
# * * * * *
# * * * *
# * * *
# * *
# *   