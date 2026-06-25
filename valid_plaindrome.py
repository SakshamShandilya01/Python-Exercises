import re

s = input("Enter a string: ")

# Remove non-alphanumeric characters and convert to lowercase
cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

if cleaned == cleaned[::-1]:
    print("Valid Palindrome")
else:
    print("Not a Palindrome")