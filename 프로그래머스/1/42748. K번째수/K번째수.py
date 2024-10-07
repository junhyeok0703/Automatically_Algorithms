def solution(array, commands):
    answer=[]
    for i in commands:
        start = i[0]-1
        end = i[1]
        a= array[start:end]
        a.sort()
        idx = i[2]
        answer.append(a[idx-1])
    return answer