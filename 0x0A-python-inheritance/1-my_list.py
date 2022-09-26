#!/usr/bin/python3
"""Module: 1-my_list
My_list class inherits from list class
"""


class MyList(list):
    """Mylist inheriting from list class
    """

    def print_sorted(self):
        """Prints sorted list
        """
        newList = sorted(self[:])
        print("{}".format(newList))
