import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    N = int(input())
    queries = []
    for _ in range(N):
        queries.append(input().split())

    queries.sort(key=len) # we want to deal with the simplest queries first
    
    # kind 0 is simple
    # kind 1 is same
    # kind 2 is different

    # if kind is 0
    # target_name is a drink
    # where 1 is coke and 2 is chocolate milk
    # if kind is 1 or 2
    # they want same as person name or different from person name
    wants = {} # name : [kind, target_name]
    drink_dict = {
        1: "Coke",
        2: "chocolate milk"
    }

    # name : drink
    given = {}

    for query in queries:
        name = query[0]
        state = query[1]
        if len(query) == 3:
            # easy wants
            if state == 'wants':
                drink = 1 if query[2] == 'Coke' else 2
            else:
                drink = 2 if query[2] == 'Coke' else 1
            wants[name] = [0, drink]
        elif len(query) == 5:
            kind = 1 if query[2] == 'same' else 2
            wants[name] = [kind, query[4]]
        else:
            wants[name] = [3, query[2], query[4], query[6]]

    
    for person, attributes in wants.items():
        kind = attributes[0]
        want = attributes[1]
        if kind == 0:
            # simple
            given[person] = drink_dict[want]
        elif kind == 1:
            if len(given) < 1:
                print('Everybody gets water')
                break
            given[person] = given[want]
        elif kind == 2:
            if len(given) < 1:
                print('Everybody gets water')
                break
            new_given = 1 if given[want] == 'chocolate milk' else 2
            given[person] = drink_dict[new_given]
        else:
            target_person = attributes[2]
            target_need_drink = attributes[3]
            if target_need_drink == given[target_person]:
                given[person] = drink_dict[want]
            else:
                given[person] = drink_dict[1]

    
    sorted_given = dict(sorted(given.items()))
    for person, drink in sorted_given.items():
        print(f'{person} gets {drink}')

if __name__ == "__main__":
    solve()
