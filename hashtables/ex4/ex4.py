def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    # Your code here
    for num in a:
        pos_int = abs(num)
        if pos_int not in cache:
            cache[pos_int] = 1
        else:
            cache[pos_int] += 1

    return [pair[0] for pair in cache.items() if pair[1] > 1]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
