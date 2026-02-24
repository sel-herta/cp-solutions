import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    N = int(input())
    plates = list(map(int, input().split()))
    
    # we can roll a N sided die, call the result i
    # the result from this die is the plate we look at
    # if plates[i] > 0, then eat from it, decrement plates[i] by 1
    # do nothing otherwise
    # at any point, we HAVE to roll a die
    # how could we make this into a dp problem? what are the states
    # this is a probability problem atp
    # i guess we can track how many plates we have finished or smthn
    # 
            
            
    

if __name__ == "__main__":
    solve()
