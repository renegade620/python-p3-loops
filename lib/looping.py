#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print(i)
        i -= 1
    return "Happy New Year!\n"

def square_integers(int_list):
    int_list = [integer * integer for integer in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    pass

# happy new year
print(happy_new_year())
# square integers
print(square_integers([1, 2, 3, 4]))
