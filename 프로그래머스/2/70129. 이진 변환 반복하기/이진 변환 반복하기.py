def solution(s):

    cnt=0
    rcnt=0
    while s != '1':
        zero_count = s.count('0')
        rcnt += zero_count
        
        s= bin(len(s.replace('0','')))[2:]
        cnt+=1
    return [cnt,rcnt]