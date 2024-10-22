def solution(s):
    answer = ''
    c_t = True
    for i in s:
        if i==' ':
            answer+=' '
            c_t = True
        elif c_t:
            answer+= i.upper()
            c_t=False
        else:
            answer+=i.lower()
            
            
    return answer