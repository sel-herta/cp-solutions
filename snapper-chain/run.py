import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    for _ in range(5):
        n, k = list(map(int, input().split()))
        if n == 1:
            # easy case
            if k % 2 == 1:
                print('ON')
            else:
                print('OFF')
        else:
            if k % (2 ** n) == ((2 ** n) - 1):
                print('ON')
            else:
                print('OFF')

if __name__ == "__main__":
    solve()
