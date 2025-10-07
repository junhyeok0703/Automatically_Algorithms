
def solution(today, terms, privacies):
    # 1. terms 배열안에서 각 요소를 공백단위로 잘라서 dict로 저장하기
    # 2. privacies 배열에서도 마찬가지
    # 3. privacies[i][0] 요소로 들을 위에 terms dict랑 매칭하면서 날짜를 계산 
    # 4. today랑 위 날짜 배열이랑 비교하면서 만약 today보다 클 경우 그 요소 인덱스+1를 해서 result에 저장해야함
    
    
    ty, tm, td = map(int, today.split('.'))

    
    term_dict = {}
    for t in terms:
        key, val = t.split(' ')
        term_dict[key] = int(val)

    
    result = []

    for idx, privacy in enumerate(privacies, start=1):  
        ymd, term_type = privacy.split(' ')
        yy, mm, dd = map(int, ymd.split('.'))

        
        mm += term_dict[term_type]

        
        yy += (mm - 1) // 12
        mm = (mm - 1) % 12 + 1

        
        if (yy, mm, dd) <= (ty, tm, td):
            result.append(idx)
    
    return result