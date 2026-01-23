# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

CheckEven = lambda No : No % 2 == 0

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Actual Data is : ", Data)

    EvenData = list(filter(CheckEven, Data))

    print("Even Numbers are : ", EvenData)

if __name__ == "__main__":
    main()

# Output is:
# Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even Numbers are :  [2, 4, 6, 8, 10]