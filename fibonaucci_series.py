n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci Series:")

if n == 1:
    print(first)

elif n >= 2:
    print(first, end=" ")
    print(second, end=" ")

    for i in range(3, n + 1):
        third = first + second
        print(third, end=" ")
        first = second
        second = third