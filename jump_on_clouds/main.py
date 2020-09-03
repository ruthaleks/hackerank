#!/bin/python3

import sys
from collections import Counter 

def read_input():
    n = int(sys.stdin.readline())
    data = tuple(map(int, sys.stdin.readlines()[0].strip().split(" ")))
    return data, n

def min_jumps(clouds):
    return clouds // 2 + 1

def jump_on_clouds(data):
    obst_idx = [i for i, v in enumerate(data) if v == 1]
    if len(obst_idx) > 0:
        diff = [obst_idx[i+1]-obst_idx[i]-1 for i in range(len(obst_idx)-1)]
        diff.insert(0, obst_idx[0]) #beginning
        diff.insert(len(diff), len(data)-obst_idx[-1]-1) # ending
        return sum(map(min_jumps, diff)) - 1
    return min_jumps(len(data)) - 1

def main():
    data, n = read_input()
    jumps= jump_on_clouds(data)
    print(jumps)

if __name__ == "__main__":
    main()
