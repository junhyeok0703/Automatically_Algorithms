def solution(s):
    answer = True
    cnt1=0
    cnt2=0
    for i in s:
        if i == "p" or i =="P":
            cnt1 += 1
        elif i == "y" or i=="Y":
            cnt2 += 1
        print(cnt1,cnt2)
    if cnt1==cnt2:
        answer=True
    else:
        answer=False
    return answer