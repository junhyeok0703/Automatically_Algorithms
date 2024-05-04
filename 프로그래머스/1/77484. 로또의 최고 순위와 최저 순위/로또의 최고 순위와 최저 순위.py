def solution(lottos, win_nums):
    
    cnt = 0
    zero_count = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
            

    max_rank = cnt + zero_count
    min_rank = cnt
    
    # 순위를 변환합니다.
    rank_converter = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6}
    max_rank = rank_converter.get(max_rank, 6)
    min_rank = rank_converter.get(min_rank, 6)
    
    return [max_rank, min_rank]
