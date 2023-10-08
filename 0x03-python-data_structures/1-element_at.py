#!/usr/bin/python3
def element_at(my_list, idx):
    """Get an element from the list

    Args:
        my_list: list
        idx: index of element to retrieve

    Returns:
        Value of eleement at index idx
    """

    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]
