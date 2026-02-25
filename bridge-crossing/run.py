import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    M = int(input())
    Q = int(input())
    people = []
    for _ in range(Q):
        name = input()
        time = int(input())
        people.append([name, time])
    # we can either
    # add person to group
    # make curr group cross bridge
    memo = {}
    def dfs(i, curr_group, person):
        if i >= len(people) or len(curr_group) > M:
            return float('inf')
        state = (i, curr_group)
        if state in memo:
            return memo[state]
        add_person = float('inf')
        leave = float('inf')
        add_person = dfs(i + 1, curr_group.append([people[i]]))
        if len(curr_group) >= 1:
            leave = max(curr_group) + dfs(i, [])
        res = min(add_person, leave)
        memo[state] = res
        return res

    
        

if __name__ == "__main__":
    solve()
