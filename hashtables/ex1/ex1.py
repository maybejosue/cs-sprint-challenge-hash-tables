def get_indices_of_item_weights(weights, length, limit):
    storage = {}

    for idx in range(length):
        other_num_to_equal_limit = abs(weights[idx] - limit)

        if other_num_to_equal_limit in storage and other_num_to_equal_limit+weights[idx] == limit:
            other_num = storage[other_num_to_equal_limit]
            print((idx, other_num))
            return (idx, other_num)
        else:
            storage[weights[idx]] = idx
    return None


# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
