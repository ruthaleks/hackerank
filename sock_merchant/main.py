#!/bin/python3

import sys
from collections import Counter 

def read_input():
    n = int(sys.stdin.readline())
    data = tuple(map(int, sys.stdin.readlines()[0].strip().split(" ")))
    return data, n

def sock_merchant(n, ar):
    counter = Counter(ar)
    return sum(map(lambda v: v // 2, counter.values()))

def main():
    data, n = read_input()
    pairs = sock_merchant(n, data)
    print(pairs)

if __name__ == "__main__":
    main()
