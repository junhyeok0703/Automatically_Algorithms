def solution(array, commands):
    answer = []
    for i in commands:
        
        i0 = i[0]-1
        i1 = i[1]
        arr = array[i0:i1].copy()
        arr1 = sorted(arr)
        i2 = i[2]-1
        answer.append(arr1[i2])
    return answer