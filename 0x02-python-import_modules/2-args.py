#!/usr/bin/python3.4
if __name__ == '__main__':
    from sys import argv

    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('1 argument:')
        print('1: {:s}'.format(argv[1]))
    elif len(argv) > 2:
        print('{:d} arguments:'.format(len(argv) - 1))
        for arg in range(1, len(argv)):
            print('{:d}: {:s}'.format(arg, argv[arg]))
