#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    i = 0
    while i < len(my_list):
        num += my_list[i][0] * my_list[i][1]
        den += my_list[i][1]
        i += 1

    return (num / den)
