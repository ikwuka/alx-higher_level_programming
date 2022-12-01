#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers != 99:
        print('{:02d}'.format(numbers), end=", ")
    else:
        print('{:d}'.format(numbers))
