import sys, math
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    t = int(input())
    for _ in range(t):
        h, w, d = list(map(int, input().split()))
        grid = []
        for _ in range(h):
            line = list(input())
            grid.append(line)
        
        rows, cols = len(grid), len(grid[0])
        sr, sc = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'X':
                    sr, sc = r, c
                    break
        
        visible = 0
        try_dirs = []
        
        for dx in range(-d, d + 1):
            for dy in range(-d, d + 1):
                if dx and dy == 0:
                    continue
                if math.gcd(abs(dx), abs(dy)) == 1:
                    try_dirs.append((dx, dy))
        print(try_dirs)
                
    
if __name__ == "__main__":
    solve()
