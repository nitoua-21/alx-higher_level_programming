#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    total_weight = 0
    for score, weight in my_list:
        total += score * weight
        total_weight += weight
    return total / total_weight
