import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    N = int(input())
    triangle = []
    for _ in range(N):
        data = list(map(int, input().split()))
        triangle.append(data)
    
    memo = {}
    def dfs(i, j):
        if i >= len(triangle):
            return 0
        state = (i, j)
        if state in memo:
            return memo[state]
        down = triangle[i][j] + dfs(i + 1, j)
        down_right = triangle[i][j] + dfs(i + 1, j + 1)
        res = max(down, down_right)
        memo[state] = res
        return res
    print(dfs(0, 0))

if __name__ == "__main__":
    solve()
