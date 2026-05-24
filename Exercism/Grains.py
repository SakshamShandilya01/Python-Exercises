def square(number):

    # Added this condition because Exercism checks
    # if the square number is between 1 and 64
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    grain = 1

    # Changed each() to range()
    # number - 1 because square 1 already has 1 grain
    for i in range(number - 1):
        grain = grain * 2

    return grain


def total():
    sum = 0

    # Added : after range()
    # Loop runs from square 1 to 64
    for i in range(1, 65):

        # Added square(i) to get grains of each square
        sum = sum + square(i)

    return sum