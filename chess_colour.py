coordinate = input("Enter coordinate: ")

letter = coordinate[0]
number = int(coordinate[1])

if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    if number % 2 == 1:
        print(False)
    else:
        print(True)

if letter == "b" or letter == "d" or letter == "f" or letter == "h":
    if number % 2 == 1:
        print(True)
    else:
        print(False)