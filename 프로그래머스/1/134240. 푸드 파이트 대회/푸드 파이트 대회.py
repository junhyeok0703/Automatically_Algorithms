def solution(food):
    ind=0
    result = ''
    for i in food:
        if i>1:
            for j in range((i-(i%2))//2):
                result +=str(ind)
        ind+=1
    result2 =''.join(reversed(result))
    result +='0'
    result+=result2
    return result