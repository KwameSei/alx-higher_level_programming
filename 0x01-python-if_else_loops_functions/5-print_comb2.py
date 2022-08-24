#!/usr/bin/python3

for a in range(0, 10):
    for b in range(a + 1, 10):
        end = ", "
        if a == 8 and b == 9:
            end = "\n"
        print("{}{}".format(a, b), end=end)
