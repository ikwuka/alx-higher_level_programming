#!/usr/bin/python3
def uppercase(str):
    answer = ''
    for letter in str:
        index = ord(letter)
        if index >= 97 and index <= 122:
            answer += chr(index - 32)
        elif index >= 65 and index <= 90:
            answer += chr(index)
        else:
            answer += chr(index)
    print('{}'.format(answer))
