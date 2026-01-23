# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements.

from functools import reduce

Maximum = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    Data = [10, 25, 7, 34, 19, 8]
    print("Actual Data is : ", Data)

    RData = reduce(Maximum, Data)
    # RData = reduce(lambda a, b: a if a > b else b, Data)

    print("Maximum Element After Reduce is : ", RData)

if __name__ == "__main__":
    main()

# Output is:
# Actual Data is :  [10, 25, 7, 34, 19, 8]
# Maximum Element After Reduce is :  34