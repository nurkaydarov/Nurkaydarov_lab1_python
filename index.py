#!/usr/bin/env python3
# coding=utf-8

import math
import re
# re.match('^[0-9]*$', numbrer)

def main():
    try:
        a = int(input("Type A: "))
        b = int(input("Type B: "))
        x = int(input("Type X: "))
        try:
            if x <= 4 and x != '':
                y = ((a ** 2) / (x ** 2)) + 6 * x
            else:
                y = (b ** 2) * math.pow((4 + x), 2)
            print("Result y = %.2f" % y)
        except:
            print("There is no solution")
    except:
        print("Program error")


if __name__ == '__main__':
    main()