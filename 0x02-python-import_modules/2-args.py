#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg = len(argv) - 1

    if arg == 0:
        print("{:d} arguments.".format(arg))
    elif arg == 1:
        print("{:d} argument:".format(arg))
        print("{:d}: {}".format(1, str(argv[1])))
    else:
        print("{:d} arguments:".format(arg))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
