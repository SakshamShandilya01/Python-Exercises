def find_the_difference(s, t):
    result = 0

    for ch in s:
        result ^= ord(ch)

    for ch in t:
        result ^= ord(ch)

    return chr(result)

# User input
s = input("Enter first string: ")
t = input("Enter second string: ")

print("Missing/Extra character:", find_the_difference(s, t))