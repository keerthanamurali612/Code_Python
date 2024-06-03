# Write a  Python program to check whether an alphabet is a vowel or consonant.

char=input("Enter the character")

vowels=['a','e','i','o','u','A','E','I','O','U']

if char in vowels:
    print(f"The character {char} is vowels")
else:
    print(f"The character {char} is consonant")