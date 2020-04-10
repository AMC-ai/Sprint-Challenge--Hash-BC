#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    link togeither source and destination tickets to reconstruct the trip starting at none by creating a new array to display them and return the flight path that was taken
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    flight_path = []
    new_ticket = hash_table_retrieve(hashtable, 'NONE')
    while new_ticket != 'NONE':
        flight_path.append(new_ticket)
        new_ticket = hash_table_retrieve(hashtable, new_ticket)
    return flight_path
