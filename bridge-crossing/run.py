import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    M = int(input())
    Q = int(input())
    people = []
    times = []
    for _ in range(Q):
        name = input()
        time = int(input())
        people.append(name)
        times.append(time)
    
    # could either make the current group leave
    # or add to the queue
    # so its like a for loop, from i up to i + M
    # dp lol
    
    leaving = []
    
    memo = {}
    def dfs(i):
        nonlocal leaving
        if i >= len(people):
            return 0
        if i in memo:
            return memo[i]
        # make the singular person leave (always valid)
        initial_leave = times[i] + dfs(i + 1)
        p1 = people[i]
        # make groups up to M leave from i
        group_leave = float('inf')
        j = i
        max_leaver = times[i]
        for k in range(1, M):
            if i + k < len(people):
                max_leaver = max(max_leaver, times[i + k])
                new = max_leaver + dfs(i + k + 1)
                if new <= group_leave:
                    group_leave = new
                    j = i + k + 1
            else:
                break
        if initial_leave < group_leave:
            leaving.append(p1)
        else:
            leaving.extend([people[i:j]])
        res = min(group_leave, initial_leave)
        memo[i] = res
        return res
    print(dfs(0))
    print(leaving)
                
        

if __name__ == "__main__":
    solve()
