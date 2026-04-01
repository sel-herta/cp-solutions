import math
import sys
from collections import Counter, defaultdict, deque

sys.setrecursionlimit(200000)


def solve():
    # silly key: a key is typed, but it displays as a different char
    # silent key: a key is typed, but it doesn't appear in the new string

    # we use the silly key at least once
    # we dont necessarily type the silent key

    # we never type the wrong letter displayed by the silly key

    # if frequency is the same and the char is different, could be silly key?
    # if frequency of a char from the original increases in the new string, it could also be silly

    # og: forloops
    # new: fxrlxxps
    # output:
    # o x
    # -

    # og: forloops
    # new: fxrlxxp
    # output:
    # o x
    # s

    # og: forloops
    # new: frlpz
    # output:
    # s z
    # o

    original_line = input()
    actual_line = input()

    o_chars = set(original_line)
    a_chars = set(actual_line)

    silly = list(a_chars - o_chars)[0]
    missing_keys = list(o_chars - a_chars)

    if len(missing_keys) == 1:
        # it's just a silly key
        print(f"{missing_keys[0]} {silly}")
        print("-")
    else:
        # it could be a silent key or a silly key
        # let c1 be silly and c2 be silent
        simulate = ""
        c1, c2 = missing_keys[0], missing_keys[1]
        for char in original_line:
            if char == c1:
                simulate += silly
            elif char is not c2:
                simulate += char
        if simulate == actual_line:
            print(f"{c1} {silly}")
            print(c2)
        else:
            print(f"{c2} {silly}")
            print(c1)


if __name__ == "__main__":
    solve()
