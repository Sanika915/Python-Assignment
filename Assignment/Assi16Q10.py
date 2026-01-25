# Write a program which accept name from user and display length of its name.
# Input: Marvellous                  Output: 10

def main():
      Count = 0
      Name = str(input("Enter Name : "))
      Count = len(Name)
      print("Length of Name is : ",Count)

if __name__ == "__main__":
   main()  

# Output is:
# Enter Name : Marvellous
# Length of Name is :  10