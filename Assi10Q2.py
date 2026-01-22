# Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output : 15 

def SumOfNaturalNumbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input())

result = SumOfNaturalNumbers(n)
print(result)

# Output is
#  Enter number : 5
#  Sum : 15