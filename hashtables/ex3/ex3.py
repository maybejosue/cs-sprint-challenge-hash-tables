def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # count the length of the array in order to
    # keep track of how many lists there are and
    # how many intersections we need to be considered truthy
    arr_len = len(arrays)
    result = []

    # create empty dict
    cache = {}

    # loop the the list of arrays
    for arr in arrays:
        # loop inside each array
        for num in arr:
            # if num is in the cache + 1
            if num in cache:
                cache[num] += 1
            else:
                # else insert it and start it off at 1
                cache[num] = 1

    for pair in cache.items():
        if pair[1] >= arr_len:
            result.append(pair[0])

    return result


# print(intersection([[1, 2, 4, 6], [1, 7, 8, 3, 2, 4], [1, 5, 6, 8, 3, 2]]))


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
