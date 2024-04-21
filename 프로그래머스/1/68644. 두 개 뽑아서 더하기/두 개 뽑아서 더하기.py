def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)): 
            if i!=j:
                answer.append(numbers[j]+numbers[i])   
    setarr = set(answer)
    sortarr= sorted(setarr)
    
    return sortarr