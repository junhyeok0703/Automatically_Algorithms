def solution(numbers, hand):
    answer = ''
    phonenum = {1:(0,0),2:(0,1),3:(0,2),
               4:(1,0),5:(1,1),6:(1,2),
               7:(2,0),8:(2,1),9:(2,2),
               '*':(3,0),0:(3,1),'#':(3,2)}
    
    lq = phonenum['*']
    rq = phonenum['#']
    
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            lq = phonenum[i]
        elif i in [3,6,9]:
            answer+='R'
            rq = phonenum[i]
        else:
            # 지금 i와 lq와 rq의 상대적 거리 구하기
            ll = abs(lq[0]-phonenum[i][0]) + abs(lq[1]-phonenum[i][1])
            print(ll)
            rr = abs(rq[0]-phonenum[i][0]) + abs(rq[1]-phonenum[i][1])
            print(rr)
            if ll>rr:
                answer+='R'
                rq=phonenum[i]
            elif ll<rr:
                answer+='L'
                lq=phonenum[i]
            elif ll==rr:
                if hand=='right':
                    answer+='R'
                    rq=phonenum[i]
                else:
                    answer+='L'
                    lq=phonenum[i]
    return answer