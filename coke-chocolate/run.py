import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve():
    
    while True:
        try:
            N = int(input())
            if N == 0: break
        except EOFError:
            break
        # N = int(input())
        queries = []
        for _ in range(N):
            queries.append(input().split())
            
        opposite = {
            "Coke": "chocolate milk",
            "chocolate milk": "Coke"
        }
        
        wants = {} # name : attributes
        
        # parse the queries
        for query in queries:
            name = query[0]
            state = query[1]
            if len(query) == 3:
                # simple want/hate
                drink = "Coke" if query[2] == "Coke" else "chocolate milk"
                if state == "hates":
                    drink = opposite[drink]
                wants[name] = [0, drink]
            elif len(query) == 5:
                # wants same/different of a person
                target_person = query[4]
                kind = 1 if query[2] == "same" else 2
                wants[name] = [kind, target_person]
            else:
                # gets x drink if target_person gets y drink
                want_drink = query[2]
                target_person = query[4]
                target_drink = query[6]
                wants[name] = [3, want_drink, target_person, target_drink]

        given = {} # name : drink
        curr_visits = set()
        def get_drink(person):
            if person in given:
                return given[person]
            if person in curr_visits: # cyclic dependency
                return "Water"
            if person not in wants:
                given[person] = "Coke"
                return "Coke"
            
            curr_visits.add(person)
            attributes = wants[person]
            kind = attributes[0]
            if kind == 0:
                drink = attributes[1]
            elif kind == 1:
                drink = get_drink(attributes[1])
            elif kind == 2:
                test_drink = get_drink(attributes[1])
                drink = "Water" if test_drink == "Water" else opposite[test_drink]
            else:
                want_drink = attributes[1]
                target_person = attributes[2]
                target_drink = attributes[3]
                what_do_they_have = get_drink(target_person)
                if what_do_they_have == "Water":
                    drink = "Water"
                elif target_drink == what_do_they_have:
                    drink = want_drink
                elif target_drink != what_do_they_have:
                    drink = opposite[want_drink]
            curr_visits.remove(person)
            given[person] = drink
            return drink

        possible = True
        for person in wants.keys():
            res = get_drink(person)
            if res == "Water":
                possible = False
                break
        
        if possible:
            sorted_given = dict(sorted(given.items()))
            for person, drink in sorted_given.items():
                print(f'{person} gets {drink}')
        else:
            print("Everybody gets water")
        print()

if __name__ == "__main__":
    solve()
