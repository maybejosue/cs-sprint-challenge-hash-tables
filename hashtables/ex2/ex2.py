#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    travel_order = []

    for item in tickets:
        cache[item.source] = item.destination

    print(cache)

    begin_value = 'NONE'
    print(begin_value)
    loop = True

    while loop:
        # get the value of the 'None' key

        # tell it to search for the value of none
        travel_order.append(cache[begin_value])

        begin_value = cache[begin_value]

        if begin_value == 'NONE':
            return travel_order
        print(f"travel_order in the while:{travel_order}")

    # if the value is none then return / stop
    print(travel_order)

    return 'hey'
