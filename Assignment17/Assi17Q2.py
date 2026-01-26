# Write a program which accept one number and display below pattern.
# Input : 5
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

def main ():
    No = int(input("Enter a Number : "))

    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()
if __name__=="__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi17Q2.py
# Enter a Number : 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *