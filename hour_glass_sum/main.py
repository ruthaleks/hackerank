import sys

def read_input():
    raw_data = sys.stdin.readlines()
    data = tuple(map(str.strip, raw_data))
    arr = [tuple(map(int,line.split(" "))) for line in data]
    return arr


def main():
    arr = read_input()
    print(arr)

if __name__ == "__main__":
    main()
