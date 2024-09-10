def solution(n, lost, reserve):
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))

    for r in reserve_only:
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)

    return n - len(lost_only)