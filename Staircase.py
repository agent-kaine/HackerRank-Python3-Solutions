import math
import os
import random
import re
import sys

def staircase(n):
    i = 1
    for i in range(1, n):
        print(' ' * (n-i-1), '#' * i)
        i += 1
    print('#' * n)

if __name__ == '__main__':
    n = int(input())
    staircase(n)
