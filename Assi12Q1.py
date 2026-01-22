# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input : a
# Output : Vowel

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.lower()
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

# Output is:
# Enter a character: a
# Vowel    