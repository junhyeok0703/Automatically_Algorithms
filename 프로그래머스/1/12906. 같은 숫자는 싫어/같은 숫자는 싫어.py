def solution(arr):
    setarr = []
    setarr.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            setarr.append(arr[i])
    
    return setarr