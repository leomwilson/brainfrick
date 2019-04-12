#/bin/env python

import fileinput

colours = {
    'white':  '\033[0m',
    'red':    '\033[31m',
    'green':  '\033[32m',
    'orange': '\033[33m',
    'blue':   '\033[34m',
    'purple':  '\033[35m'
}

c = []
l = []
arr = [0]
pointer: int = 0
out = ''

for ln in fileinput.input(): # get a list of the executeable characters in the file
    for ch in ln:
        if ch in "+-<>[],.":
            c.append(ch)
print(colours['green'] + 'Compressed code: ' + colours['blue'] + ''.join(c) + colours['white'])

stop_all = input(colours['green'] + 'Stop for input/output only [y/N]?' + colours['white']).lower() != 'y'

i = 0 # the for loop might not look python-y, but this is neccessary for loops
while i < len(c): # interpret the file, step by step
    ch = c[i]
    print(colours['green'] + 'Running char: ' + colours['blue'] + ch + colours['green'] + ' (' + colours['orange'] + str(i) + colours['green'] + ') [' + colours['orange'] + str(len(l)) + colours['green'] + ']' +colours['white'])
    if ch == '>':
        pointer += 1
        if pointer == len(arr): # prevent IndexError
            arr.append(0)
    elif ch == '<':
        pointer -= 1
        if pointer < 0:
            print(colours['red'] + 'Invalid syntax: pointer cannot be negative')
    elif ch == '+':
        arr[pointer] += 1
    elif ch == '-':
        arr[pointer] -= 1
    elif ch == '[':
        l.append(i + 1)
    elif ch == ']':
        if arr[pointer] == 0:
            del l[-1]
        else:
            i = l[-1] - 1 # -1 makes it +0 when i += 1
    elif ch == ',':
        val = input(colours['green'] + 'Input (#XXX for a decimal number): ' + colours['white'])
        if(val[0] == '#' and len(val) > 1): # handle numbers
            arr[pointer] += int(val[1:])
        else: # ascii value of char
            arr[pointer] += ord(val[0])
    elif ch == '.':
        out += chr(arr[pointer])
        print(colours['green'] + 'Output: ' + colours['white'] + chr(arr[pointer]) + colours['orange'] + ' (' + str(arr[pointer]) + ')' + colours['white'])
    print(colours['green'] + 'Values (Anything not listed is zero):' + colours['white'])
    r = ''
    for p, v in enumerate(arr):
        if v != 0:
            r += colours['green'] + ('' if r == '' else ' | ') + 'arr[' + colours['orange'] + str(p) + colours['green'] + '] = ' + colours['orange'] + str(v)
    print(r)
    if stop_all or ch == '.':
        input(colours['purple'] + 'Press enter to continue.' + colours['white'])
    i += 1
print(colours['green'] + 'Program done. Output: ' + colours['white'] + out)
input(colours['purple'] + 'Press enter to continue.' + colours['white'])