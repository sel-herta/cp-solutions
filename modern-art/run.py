import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    rows, cols = int(input()), int(input())
    moves = int(input())
    
    # if painted number is even, its black.
    # if painted number is odd, its gold.
    
    # so basically, if row and col are differing (odd vs even) its gonna be gold
    
    rows_color = [0 for _ in range(rows)]
    cols_color = [0 for _ in range(cols)]
    
    for _ in range(moves):
        op1, op2 = input().split()
        op2 = int(op2) - 1
        if op1 == 'R':
            rows_color[op2] += 1
        else:
            cols_color[op2] += 1
            
    odd_rows = 0
    odd_cols = 0
    for i in range(rows):
        if rows_color[i] % 2 == 1:
            odd_rows += 1
    for i in range(cols):
        if cols_color[i] % 2 == 1:
            odd_cols += 1
    gold = (odd_rows * (cols - odd_cols)) + (odd_cols * (rows - odd_rows))
    print(gold)
            
            
    

if __name__ == "__main__":
    solve()
