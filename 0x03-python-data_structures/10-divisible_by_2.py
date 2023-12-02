#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x_bool = my_list[:]
    for y, i in enumerate(my_list):
        if i % 2 == 0:
           x_bool[y] = True
        else:
           x_bool[y]= False
    return (x_bool)
