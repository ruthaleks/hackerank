import itertools as it
import sys

def read_input():
    n, d = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    a = tuple(map(int,sys.stdin.readline().strip().split(" ")))
    return n, d, a

def left_rot(n, d, a):
    d = {(n - d + i)%n : a[i] for i in range(n)}
    return [d[i] for i in range(n)]

def left_rot_2(n, d, a):
    return list(it.islice(it.cycle(a), d, d+n))

def main():
    n, d, a = read_input()
    res = left_rot_2(n, d, a)
    print(res)

if __name__ == "__main__":
    main()
