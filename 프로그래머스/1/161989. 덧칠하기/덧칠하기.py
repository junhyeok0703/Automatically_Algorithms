def solution(n, m, section):
    answer = 0
    i = 0
    while i < len(section):
        answer += 1 
        start = section[i]
        
        max_coverage = start + m - 1
        
       
        while i < len(section) and section[i] <= max_coverage:
            i += 1
    
    return answer
