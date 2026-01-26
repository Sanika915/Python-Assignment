# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
# Input List = [5,2,3,4,3,4,1,2,8,10]
# List after filter = [2,4,4,2,8,10]
# List after map = [4,16,16,4,64,100]
# Output of reduce = 204

from functools import reduce

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    print("Actual Data is : ", Data)

    FilterData = list(filter(lambda No: No % 2 == 0, Data))
    print("List After filter:", FilterData)

    MapData = list(map(lambda No: No ** 2, FilterData))
    print("List After map:", MapData)

    Result = reduce(lambda A, B: A + B, MapData)
    print("Output of reduce:", Result)

if __name__ == "__main__":
    main()

# Output is :
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi19Q4.py
# Actual Data is :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List After filter: [2, 4, 4, 2, 8, 10]
# List After map: [4, 16, 16, 4, 64, 100]
# Output of reduce: 204