# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains thre numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each numbers by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# Input List = [2,70,11,10,17,23,31,77]
# List after filter = [2,11,17,23,31]
# List after map = [4,22,34,46,62]
# Output of reduce = 62

from functools import reduce

def IsPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]
    print("Actual Data is : ", Data)

    FilterData = list(filter(IsPrime, Data))
    print("List After filter:", FilterData)

    MapData = list(map(lambda No: No * 2, FilterData))
    print("List After map:", MapData)

    Result = reduce(lambda A, B: A if A > B else B, MapData)
    print("Output of reduce:", Result)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi19Q5.py
# Actual Data is :  [2, 70, 11, 10, 17, 23, 31, 77]
# List After filter: [2, 11, 17, 23, 31]
# List After map: [4, 22, 34, 46, 62]
# Output of reduce: 62