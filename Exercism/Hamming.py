def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    distance = 0

    zip(strand_a,strand_b) # compare 2 string character of same index one by one

    for a,b in zip(strand_a,strand_b):
        if a!=b:
            distance +=1

    return distance