def solution(s):
    # 1. 작은 길이부터 추가 된거를 뒤로 append하면 된다.
    temp = ""
    answer=[]
    sets = s.strip('{}').split('},{')
    tuple_sets = [list(map(int, x.split(','))) for x in sets]
    sort_list = sorted(tuple_sets, key=len)
    # print(sort_list)
    for sublist in sort_list:
        for num in sublist:
            if num not in answer:
                answer.append(num)
                # print(answer)
    
    return answer