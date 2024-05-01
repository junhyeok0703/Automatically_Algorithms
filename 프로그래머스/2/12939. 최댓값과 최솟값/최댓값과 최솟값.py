
def solution(s):
    numbers = s.split() # 공백단위로 문자열 분리됨
    arr = []
    for num in numbers:
        arr.append(int(num))
    arr.sort()
    
    return f"{arr[0]} {arr[-1]}"