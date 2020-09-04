#!/bin/python3

import sys
from collections import Counter 
from itertools import accumulate
from functools import reduce 

def read_input():
    n = int(sys.stdin.readline())
    data = sys.stdin.readlines()
    return data[0].strip(), n

def repeat_string(n, s):
    print("n = ", n)
    print("string = ", s)
    c = Counter(s)
    print(c)
    print(c["a"])
    # part 1 
    num_of_s = n // len(s)
    print("number of whole s in n: ", num_of_s)
    num_a = num_of_s * c['a']
    print("number of a's exluding the rest: ", num_a)
    # part 2, the rest
    rest = n % len(s)
    print("rest:  ", rest)
    a_in_string = [1 for i in range(rest) if s[i] == "a"]
    print("rest of a's: ", len(a_in_string))
    return num_a + len(a_in_string)
    

def main():
    data, n = read_input()
    print(repeat_string(n, data))

if __name__ == "__main__":
    main()
