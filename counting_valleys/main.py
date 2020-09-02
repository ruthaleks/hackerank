#!/bin/python3

import sys
from collections import Counter 
from itertools import accumulate
from functools import reduce 

def read_input():
    n = int(sys.stdin.readline())
    data = sys.stdin.readlines()
    return data[0].strip(), n

def counting_valleys(n, s):
    top = tuple(accumulate(map(lambda x: 1 if x == 'U' else -1  , s)))
    print(top) 
    idx = top.index(0)
    valleys = 0
    if top[0] < 0:
        valleys += 1

    while idx < len(top)-1:
        if top[idx+1] < 0:
            valleys += 1
        idx = top.index(0, idx+1)

    return valleys

def main():
    data, n = read_input()
    print(data) 
    print(counting_valleys(n, data))

if __name__ == "__main__":
    main()
