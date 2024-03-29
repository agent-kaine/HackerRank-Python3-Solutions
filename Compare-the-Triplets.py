import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    ar = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            ar[0] += 1
        if b[i] > a[i]:
            ar[1] += 1
    return ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
