from collections import Counter

def solution(participant, completion):
    count_participant = Counter(participant)
    count_completion = Counter(completion)
    for person in count_participant:
        if count_participant[person] != count_completion[person]:
            return person