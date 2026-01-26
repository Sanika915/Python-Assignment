#Design a Python application that creates two threads named Prime and NonPrime
#Both threads accept a list of integers
#The Prime thread should display all prime numbers from the list
#The NonPrime thread should display all non-prime numbers from the list 
import threading

def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def ListPrime(Data):
    print("Prime Numbers : ")
    for i in (Data):
        if ChkPrime(i):
          print(i)
          
def NonPrimeList(Data):
    print("Non-Prime Numbers : ")
    for i in Data:
        if not ChkPrime(i):
          print(i)

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value) 

    t1 = threading.Thread(target=ListPrime, args=(Data,))
    t2 = threading.Thread(target=NonPrimeList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi21Q1.py
# Enter the number of elements :
# 9
# Enter the elements :
# 6
# 8
# 5
# 4
# 3
# 2
# 1
# 91
# 2
# Prime Numbers :
# Non-Prime Numbers :
# 6
# 8
# 4
# 91
# 5
# 3
# 2
# 1
# 2