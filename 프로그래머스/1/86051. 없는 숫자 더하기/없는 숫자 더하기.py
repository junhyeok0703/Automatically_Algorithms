def solution(numbers):
    answer = 0
    nums = [0,1,2,3,4,5,6,7,8,9]
    a = False
    for i in range(len(nums)):
        a=False
        for j in range(len(numbers)):
            if nums[i]==numbers[j]:
                a = True   
        if a!=True:
            answer+=nums[i]
            
            
            
    return answer