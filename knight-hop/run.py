import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    # bfs wirth edge weights of 1
    # shortest path problem
    start_pos = tuple(map(int, input().split()))
    goal_pos = tuple(map(int, input().split()))
    
    q = deque()
    seen = set()
    
    q.append((start_pos, 0))
    seen.add(start_pos)
    
    moves = [
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2)
    ]
    
    def can_visit(x, y):
        return (1 <= x <= 8 and 1 <= y <= 8) and (x, y) not in seen
    
    while q:
        node = q.popleft()
        if node[0] == goal_pos:
            print(node[1])
            break
        sx, sy = node[0]
        for nx, ny in moves:
            new = (sx + nx, sy + ny)
            if can_visit(new[0], new[1]):
                seen.add(new)
                q.append((new, node[1] + 1))
    
if __name__ == "__main__":
    solve()
