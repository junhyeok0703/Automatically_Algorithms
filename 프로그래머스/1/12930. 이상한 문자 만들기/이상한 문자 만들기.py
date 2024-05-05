def solution(s):
    answer = ''
    words = s.split(" ")  
    
    for idx, word in enumerate(words):  
        new_word = ''  
        for i in range(len(word)):  
            if i % 2 == 0:  
                new_word += word[i].upper()  
            else:  
                new_word += word[i].lower()  
        answer += new_word  
        if idx != len(words) - 1:  
            answer += ' '
    
    return answer

