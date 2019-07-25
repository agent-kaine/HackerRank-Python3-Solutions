import math
import os
import random
import re
import sys

def plusMinus(arr):
    ar = [0, 0, 0]
    l = len(arr)
    for i in arr:
        if i > 0:
            ar[0] += 1
        elif i < 0:
            ar[1] += 1
        else:
            ar[2] += 1
    print(ar[0] / l)
    print(ar[1] / l)
    print(ar[2] / l)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
