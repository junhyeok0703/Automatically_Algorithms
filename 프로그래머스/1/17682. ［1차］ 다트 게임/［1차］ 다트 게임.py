def solution(dartResult):
    score=[]
    temp_score=0
    prev_score=0     
    for char in dartResult:
        if char.isdigit():
            temp_score = temp_score * 10 +int(char)
        elif char == "S":
            score.append(temp_score)
            temp_score=0
        elif char == "D":
            score.append(temp_score**2)
            temp_score=0
        elif char == "T":
            score.append(temp_score**3)
            temp_score=0
        elif char =="*":
            score[-1] *=2
            if len(score) >=2:
                score[-2]*=2
        elif char  =="#":
            score[-1]*=-1
            
    return sum(score)