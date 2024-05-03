def solution(x):
    answer = True
    sum = 0
    for num in str(x):
        sum +=int(num)
    
    if x%sum==0:
        answer=True
    else:
        answer=False
    return answer