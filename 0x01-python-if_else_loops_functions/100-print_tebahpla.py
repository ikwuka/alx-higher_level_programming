#!/usr/bin/python3
answer = ''
for index in range(122, 96, -1):
    if index % 2:
        answer += chr(index - 32)
    else:
        answer += chr(index * 1)
print('{}'.format(answer), end='')
