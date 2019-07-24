import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    l = len(arr)
    s1 = 0; s2 = 0;
    for i in range(l):
        s1 += arr[i][i]
        s2 += arr[i][l-i-1]
    return abs(s1 - s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
