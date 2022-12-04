#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    numb = 0
    for index in argv[1:]:
        numb += int(index)
    print('{:d}'.format(numb))
