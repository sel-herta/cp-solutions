import sys
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(200000)

def solve():
    N = int(input())
    plates = list(map(int, input().split()))
    sushi_freq = {
        1: 0,
        2: 0,
        3: 0
    }
    for sushi in plates:
        sushi_freq[sushi] += 1
    
    # we can roll a N sided die, call the result i
    # the result from this die is the plate we look at
    # if plates[i] > 0, then eat from it, decrement plates[i] by 1
    # do nothing otherwise
    # at any point, we HAVE to roll a die
    # how could we make this into a dp problem? what are the states
    # this is a probability problem atp
    # i guess we can track how many plates we have finished or smthn
    # note the constraints where a dish can have 1-3 pieces of sushi
    # so maybe the state is
    # dp(ones, twos, threes) where ones twos and threes is the plates containing that amount of sushi
    # we rly only care about the frequency of said plates
    # so order doesnt matter at all
    
    # base case is easy. if we don't have any plates containing sushi we return 0
    # dp transition hard tho cuz wtf is it
    # suppose we are at dp(ones, twos, threes)
    # what is the probability of rolling a dice that has three sushi in it?
    # threes / (ones + twos + threes + zeros)
    # where zeros = N - ones - twos - threes
    # which is basically just
    # threes / N lol
    # so say we roll a dice that lands on sushi of 3 plates
    # 3 -= 1
    # 2 += 1
    # so if we pick 3
    # (three / N) * dp(ones, twos + 1, threes - 1)
    # do same thing for rolling a plate that has 2 and 1
    # for 0, we do nothing
    # but if we do nothing, the subproblem doesn't decrease so we will forever run the recursion???
    
    memo = {}
    def dfs(ones, twos, threes):
        if ones == 0 and twos == 0 and threes == 0:
            return 0
        state = (ones, twos, threes)
        if state in memo:
            return memo[state]
        one, two, three = 0, 0, 0
        zeros = N - ones - twos - threes
        if threes > 0:
            three = threes * dfs(ones, twos + 1, threes - 1)
        if twos > 0:
            two = twos * dfs(ones + 1, twos - 1, threes)
        if ones > 0:
            one = ones * dfs(ones - 1, twos, threes)
        res = (N + three + two + one) / (N - zeros)
        memo[state] = res
        return res
    print(dfs(sushi_freq[1], sushi_freq[2], sushi_freq[3]))
    
            
    

if __name__ == "__main__":
    solve()
