#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    check the table for the item
    if the item exists return item
    if the item donest exist then insert key/values in to table
    """
    for i in range(length):
        item = hash_table_retrieve(ht, limit - weights[i])
        print(f'Item Weight {item}')
        if (item is not None):
            return (i, item)
        else:
            hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
