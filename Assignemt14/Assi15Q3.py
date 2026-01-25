# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

CheckOdd = lambda No : No % 2 != 0

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Actual Data is : ", Data)

    OddData = list(filter(CheckOdd, Data))
    print("Odd Numbers are : ", OddData)

if __name__ == "__main__":
    main()

# Output is:
# Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Odd Numbers are :  [1, 3, 5, 7, 9]