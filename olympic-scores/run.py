import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    scores = []
    for _ in range(5):
        scores.append(int(input()))
    multiplier = int(input())
    total = (sum(scores) - max(scores) - min(scores)) * multiplier
    print(total)
        

if __name__ == "__main__":
    solve()
