def solution(players, m, k):
    cnt=0
    ongoing = [0]*24

    for i in range(24):
        needed = players[i] // m
        running = ongoing[i]
        
        if needed > running:
            add = needed - running
            cnt += add
            for j in range(i,min(i+k,24)):
                ongoing[j] += add
    return cnt