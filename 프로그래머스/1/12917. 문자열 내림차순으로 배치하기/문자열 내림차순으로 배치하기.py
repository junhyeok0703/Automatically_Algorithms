def solution(s):
    answer = []
    for char in s:
        answer.append(ord(char))
    answer.sort(reverse=True)
    
    result= ''
    for num in answer:
        result+=chr(num)
    return result