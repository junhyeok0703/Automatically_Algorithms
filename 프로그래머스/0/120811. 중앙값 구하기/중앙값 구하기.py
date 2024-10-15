import math
def solution(array):
    answer = 0
    arr1 = sorted(array)
    answer = arr1[math.floor(len(arr1)/2)]
    
    return answer