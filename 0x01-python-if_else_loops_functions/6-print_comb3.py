#!/usr/bin/python3
for numbers in range(0, 100):
    digit1 = numbers / 10
    digit2 = numbers % 10
    if numbers == 89:
        print('{:d}'.format(numbers))
    elif digit1 < digit2:
        print('{:02d}'.format(numbers), end=", ")
