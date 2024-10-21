def solution(array):
    count = [0]*1001
    for i in array:
        count[i] +=1
    maxx = max(count)
    cnt = 0
    c =0
    for i in range(len(count)):
        if maxx==count[i]:
            cnt+=1
            c=i
    if cnt==1:
        answer=c
    else:
        answer=-1
    return answer