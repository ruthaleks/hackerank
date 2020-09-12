import sys
import itertools 

def read_input():
    raw_data = sys.stdin.readlines()
    data = tuple(map(str.strip, raw_data))
    arr = [tuple(map(int,line.split(" "))) for line in data]
    return arr

# y/x . .
# .
# .
# x=[0, 3]
# y=[0, 3]
def hour_glass_sum(arr, c):
    y = c[0]
    x = c[1]
    #print(arr[y][x:x+3])
    #print(arr[y+1][x+1])
    #print(arr[y+2][x:x+3])
    return sum(arr[y][x:x+3]) + arr[y+1][x+1] + sum(arr[y+2][x:x+3]) 

def max_hour_glass_sum(arr): 
    idx = [i for i in range(4)]
    c = list(itertools.product(idx,idx))
    return max([hour_glass_sum(arr, i) for i in c])



def main():
    arr = read_input()
    print(max_hour_glass_sum(arr))

if __name__ == "__main__":
    main()
