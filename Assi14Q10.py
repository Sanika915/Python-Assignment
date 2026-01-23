# Write a lambda function which accept three numbers and returns largest number.

Maximum = lambda No1, No2, No3 : max(No1, No2, No3)

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    print("Enter Third Number : ")
    Value3 = int(input())

    Ret = Maximum(Value1, Value2, Value3)

    print("Largest Number is :", Ret)

if __name__ == "__main__":  
    main()

# Output is :
# Enter First Number :
# 9
# Enter Second Number :
# 3
# Enter Third Number :
# 5
# Largest Number is : 9