def solution(t, p):
    p_len = len(p)
    cnt=0
    for i in range(len(t)-p_len+1):
        tt = t[i:i +p_len]
        print(tt)
        if int(tt)<=int(p):
            cnt=cnt+1
    
    return cnt

