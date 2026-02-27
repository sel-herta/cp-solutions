import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    moves = int(input())
    pos = [0, 0]
    seen = set()
    seen.add((0, 0))
    ans = 0
    
    dirs = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    for _ in range(moves):
        move = input()
        dir = move[0]
        amount = int(move[1:len(move)])
        for _ in range(amount):
            pos[0] += dirs[dir][0]
            pos[1] += dirs[dir][1]
            if (pos[0], pos[1]) in seen:
                ans += 1
            seen.add((pos[0], pos[1]))
    print(ans)
        

if __name__ == "__main__":
    solve()
