# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

String = lambda a : len(a) > 5

def main():
    Data = ["Shreya", "Shruti", "Riya", "Sanika", "Ishvari"]
    print("Actual Data is : ", Data)

    FData = list(filter(String, Data))

    print("Data After Filter is : ", FData)

if __name__ == "__main__":
    main()

# Output is:
# Actual Data is :  ['Shreya', 'Shruti', 'Riya', 'Sanika', 'Ishvari']
# Data After Filter is :  ['Shreya', 'Shruti', 'Sanika', 'Ishvari']