import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    
    # given n list of integers
    # find out if a pair exists that are similar
    # in this case, similar seems to mean they are of the same order
    # 1 2 3 4 5 6 and 4 3 2 1 6 5 are similar
    
    # initial thought was to find permutations of the first snowflake, but that would violate the clockwise/counterclockwise order
    
    # maybe we want to convert everything to be clockwise, which is a pretty easy thing to do
    # compare middle element of A to the first element of A, if A[m] > A[0] then we chill, otherwise we should reverse the array to turn it clockwise
    
    # okay but maybe not lmao, seems too be too many layers for that
    # well since we are guaranteed 6 integers and not a million, we can maybe
    # do O(6) work for each snowflake
    # use the first snowflake as a reference point, but what if that snowflae
    # doesn't end up being a pair and some other snowflake is a pair
    # ah crap now thats O(n^2)
    
    
    
    n = int(input())
    snowflakes = []
    
        

if __name__ == "__main__":
    solve()
