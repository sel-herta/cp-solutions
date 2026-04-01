import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)


def solve():
    N, M = map(int, input().split())
    lights = list(map(int, input().split()))
    people = list(map(int, input().split()))

    lights.sort()
    people.sort()

    min_cost = 0
    if people[0] < lights[0]:
        min_cost += lights[0] - people[0]
    if people[-1] > lights[-1]:
        min_cost += people[-1] - lights[-1]

    track = 0
    for i in range(N - 1):
        left = lights[i]
        right = lights[i + 1]
        gap = 0
        last = left
        while track < M and people[track] < right:
            if people[track] > left:
                gap = max(gap, people[track] - last)
                last = people[track]
            track += 1
        gap = max(gap, right - last)
        min_cost += (right - left) - gap

    print(min_cost)


if __name__ == "__main__":
    solve()
