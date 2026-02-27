import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    parking_spots = int(input())
    lights = int(input())
    questions = int(input())
    
    shined_spots = [0 for _ in range(parking_spots)]
    
    for _ in range(lights):
        spot, reach = list(map(int, input().split()))
        spot -= 1
        if spot - reach >= 0:
            shined_spots[spot - reach] += 1 # start
        else:
            shined_spots[0] += 1
        if spot + reach + 1 < parking_spots:
            shined_spots[spot + reach + 1] -= 1 # end
    
    prefix = [0 for _ in range(parking_spots + 1)]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + shined_spots[i-1]
    
    for _ in range(questions):
        if prefix[int(input())] > 0:
            print('Y')
        else:
            print('N')

if __name__ == "__main__":
    solve()
