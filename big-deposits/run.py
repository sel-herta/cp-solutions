import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    percent, years, min_coins = list(map(int, input().split()))
    
    grow_percent = 1 + (percent / 100)
    
    # find N
    # where N is the min coin to deposit to bank each year
    # binary search?
    
    l, r = 0, min_coins
    ans = 0
    
    while l <= r:
        try_n = (l + r) // 2
        # try this
        total = 0
        for _ in range(1, years + 1):
            total = (total + try_n) * (100 + percent) // 100
            if total >= min_coins:
                break
        if total >= min_coins:
            ans = try_n
            r = try_n - 1
        else:
            l = try_n + 1
    print(ans)
        
        
    
            
if __name__ == "__main__":
    solve()
