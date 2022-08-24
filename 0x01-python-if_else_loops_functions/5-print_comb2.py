#!/usr/bin/python3

for a in range(0, 100):
        end = ", "
        if a == 99:
            end = "\n"

        if a < 10:
            print(f"0{a}", end=end)
        else:
            print(f"{a}", end=end)
