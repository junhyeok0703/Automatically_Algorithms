def solution(num):
    cnt = 0
    
    while(True):
        if num==1:
            return cnt
        if cnt==500:
            return -1
        if num%2==0:
            num=int(num)/2
            cnt+=1
        elif num%2==1:
            num=int(num)*3
            num=int(num)+1
            cnt+=1