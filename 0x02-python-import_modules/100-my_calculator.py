#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        c = argv[2]
        op = {'+': add, '-': sub, '*': mul, '/': div}
        for index in op:
            if c == index:
                print('{} {} {} = {}'.format(a, c, b, op[index](a, b)))
                exit(0)
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
