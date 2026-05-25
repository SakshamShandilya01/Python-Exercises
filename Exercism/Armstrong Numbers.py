def is_armstrong_number(number):
    original_number = number
    count = 0

    temp = number

    while temp > 0:
        temp = temp // 10
        count += 1

    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp = temp // 10

    return total == original_number