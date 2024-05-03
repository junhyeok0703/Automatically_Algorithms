def solution(s):
    answer = 0
    while s:
        x = s[0]
        cnt_x = 0
        cnt_not_x = 0
        for i in range(len(s)):
            if s[i] == x:
                cnt_x+=1
            else:
                cnt_not_x+=1
                
            if cnt_x==cnt_not_x:
                answer+=1
                s = s[i+1:]
                break
        else:
            if s:
                answer+=1
            break
    return answer
