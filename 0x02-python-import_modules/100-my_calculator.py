#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv) - 1
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:

        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == "/":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
        elif operator == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
