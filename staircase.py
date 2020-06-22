#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n-1, -1, -1):
        for j in range(0, n):
            if i > j:
                print(' ', end='')
            else:
                print('#', end='')
        print('')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
