#!/usr/bin/python3

for n in range(122, 96, -1):
    m = 32
    if n % 2 == 0:
        m = 0

    print("{}".format(chr(n - m)), end="")
