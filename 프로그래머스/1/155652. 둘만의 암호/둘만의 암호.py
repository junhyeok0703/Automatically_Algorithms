def solution(s, skip, index):
    answer=''
    for i in s:
        cnt = index
        while cnt>0:
            if i=='z':
                i='a'
            else:
                i = chr(ord(i)+1)
            if i not in skip:
                cnt-=1
        answer+=i
    return answer