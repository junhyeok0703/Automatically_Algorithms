def solution(s, n):
    answer = ''
    for char in s:
        shifted_char = ord(char) + n
        if char.isupper():
            if shifted_char > ord('Z'):
                shifted_char -= 26
        elif char.islower():
            if shifted_char > ord('z'):
                shifted_char -= 26
        else:
            answer += char
            continue
        answer += chr(shifted_char)
    return answer

print(solution("AB", 1))  
