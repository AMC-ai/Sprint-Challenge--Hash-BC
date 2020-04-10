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
    iterate through tickets objects and insert into hashtable (flight_path)
    link togeither source and destination tickets to reconstruct the trip starting at none by creating a new array to display them and return the flight path that was taken
    """
    # iterate through
    for ticket in tickets:
        # using function to "link the ticket objects together"
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # new table to display reconstructed flight path
    flight_path = []
    # gives us the origin
    new_ticket = hash_table_retrieve(hashtable, 'NONE')
    # appends destination ticket to source ticket in order set in the new table
    while new_ticket != 'NONE':
        flight_path.append(new_ticket)
        new_ticket = hash_table_retrieve(hashtable, new_ticket)
    return flight_path
