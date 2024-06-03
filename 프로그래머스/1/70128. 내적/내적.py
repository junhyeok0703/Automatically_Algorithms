def solution(a, b):
    answer = 0
    for q,w in zip(a,b):
        answer += q*w
    return answer