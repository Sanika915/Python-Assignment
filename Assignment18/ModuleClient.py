from MarvellousNum import ChkPrime

def ListPrime(Data):
    Sum = 0

    for No in Data:
        if ChkPrime(No):
            Sum = Sum + No

    return Sum


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []
    print("Enter the elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Result = ListPrime(Data)
    print("Addition of prime numbers is :", Result)


if __name__ == "__main__":
    main()
