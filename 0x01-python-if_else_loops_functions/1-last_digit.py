#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = abs(number) % 10
if number < 0:
    numb = -(numb)
if numb > 5:
    print(f"Last digit of {number} is {numb} and is greater than 5")
elif numb < 6 and numb != 0:
    print(f"Last digit of {number} is {numb} and is less than 6 and not 0")
elif numb == 0:
    print(f"Last digit of {number} is {numb} and is 0")
