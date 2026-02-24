import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    pair_dict = {
        "p":"q",
        "q":"p",
        "d":"b",
        "b":"d"
    }
    
    print("Ready")
    while True:
        pair = input()
        if pair == "  ":
            break
        if pair[0] in pair_dict and pair[1] == pair_dict[pair[0]]:
            print("Mirrored pair")
        else:
            print("Ordinary pair")
        

if __name__ == "__main__":
    solve()
