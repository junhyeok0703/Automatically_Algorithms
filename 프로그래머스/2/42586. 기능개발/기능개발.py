def solution(progresses, speeds):
    cnt = []
    for i in range(len(progresses)):
        days = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        
        cnt.append(days)
    print(cnt)
    cnt2 = []
    front = cnt[0]
    count=1
    for i in range(1,len(cnt)):
        if cnt[i]<=front:
            count+=1
        else:
            cnt2.append(count)
            front = cnt[i]
            count=1
            
    cnt2.append(count)
    return cnt2