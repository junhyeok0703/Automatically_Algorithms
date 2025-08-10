from itertools import combinations

def solution(number):
    count = 0
    for trio in combinations(number, 3): 
        if sum(trio) == 0:
            count += 1
    return count