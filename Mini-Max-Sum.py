import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum - max(arr), sum - min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
