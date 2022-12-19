#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for index in range(0, x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            cont = cont + 1
        except (ValueError, TypeError):
            pass
    print()
    return cont
