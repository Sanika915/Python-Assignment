#Design a Python application that creates two threads
#Thread1 should find maximum element from a list
#Thread2 should find minimum element from the same list
#List should be accepted from user
import threading

def MaxList(Data):
  Max = Data[0]
  for i in Data:
        if i > Max:
           Max = i
  print("Maximum Number is :", Max)

def MinList(Data):
    Min = Data[0]
    for i in Data:
        if i < Min:
            Min = i
    print("Minimum Number is :", Min)

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

    t1 = threading.Thread(target=MaxList, args=(Data,))
    t2 = threading.Thread(target=MinList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi21Q2.py
# Enter the number of elements :
# 1
# Enter the elements :
# 2
# Maximum Number is : 2
# Minimum Number is : 2