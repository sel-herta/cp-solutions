import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    buy = int(input())
    total_tickets = int(input())
    people_bought = int(input())
    
    total_tickets -= people_bought
    if buy > total_tickets:
        print("N")
    else:
        print(f"Y {total_tickets - buy}")
        

if __name__ == "__main__":
    solve()
