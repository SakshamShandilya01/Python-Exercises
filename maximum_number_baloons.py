def maxNumberOfBalloons(text):
    count_b = 0
    count_a = 0
    count_l = 0
    count_o = 0
    count_n = 0

    for ch in text:
        if ch == 'b':
            count_b += 1
        elif ch == 'a':
            count_a += 1
        elif ch == 'l':
            count_l += 1
        elif ch == 'o':
            count_o += 1
        elif ch == 'n':
            count_n += 1

    return min(count_b, count_a, count_l // 2, count_o // 2, count_n)


text = input("Enter a string: ")
print(maxNumberOfBalloons(text))