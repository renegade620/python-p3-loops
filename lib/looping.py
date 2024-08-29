#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    int_list = [integer * integer for integer in int_list]
    return int_list


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# happy new year
print(happy_new_year())
# square integers
print(square_integers([1, 2, 3, 4]))
# # fizzbuzz
fizzbuzz()


