def intersection(arrays):
    arr_len = len(arrays)
    result = []

    cache = {}

    for arr in arrays:
        for num in arr:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

    for pair in cache.items():
        if pair[1] >= arr_len:
            result.append(pair[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
