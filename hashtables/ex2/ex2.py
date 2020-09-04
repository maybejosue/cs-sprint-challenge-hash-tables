#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    travel_order = []

    for item in tickets:
        cache[item.source] = item.destination

    begin_value = 'NONE'
    loop = True

    while loop:
        travel_order.append(cache[begin_value])

        begin_value = cache[begin_value]

        if begin_value == 'NONE':
            return travel_order

    return 'hey'
