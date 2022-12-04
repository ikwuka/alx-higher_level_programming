#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for index in dir(hidden_4):
        if index in dir(hidden_4):
            if index[:2] != '__':
                print('{}'.format(index))
