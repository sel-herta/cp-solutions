import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    N = int(input())
    queries = []
    for _ in range(N):
        queries.append(input().split())
    
    # 1 is coke
    # 2 is chocolate milk
    easy_wants = {} # name : drink
    
    # kind 1 is same
    # kind 2 is different
    bruh_wants = {} # name : [kind, target_name]

    for query in queries:
        name = query[0]
        state = query[1]
        if len(query) == 3:
            # easy wants
            if state == 'wants':
                drink = 1 if query[2] == 'Coke' else 2
            else:
                drink = 2 if query[2] == 'Coke' else 1
            easy_wants[name] = drink
        else:
            kind = 1 if query[2] == 'same' else 2
            bruh_wants[name] = [kind, query[4]]
    
    print(easy_wants)
    print(bruh_wants)

if __name__ == "__main__":
    solve()
