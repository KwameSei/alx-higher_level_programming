#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    bool_list = []

    even_num = my_list[0]
    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return (bool_list)
