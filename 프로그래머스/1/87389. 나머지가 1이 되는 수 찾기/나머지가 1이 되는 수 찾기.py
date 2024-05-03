def solution(n):
    answer = 0
    for i in range(n):
        x=i+1
        if(n%x==1):
            answer=i+1
            break
    return answer