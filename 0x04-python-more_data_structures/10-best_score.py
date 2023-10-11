#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.values()) == 0:
        return None
    max_score = max(a_dictionary.values())
    for key, val in a_dictionary.items():
        if val == max_score:
            return key
