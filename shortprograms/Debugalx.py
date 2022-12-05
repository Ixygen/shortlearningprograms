#!/usr/bin/python3
for lower in range(97, 123):
    for upper in range(65, 91):
        if lower != upper:
            print(chr(lower))
            print(chr(upper))

