import math

def solution(n):
    result=0
    sqrt_n = math.sqrt(n)
    
    if sqrt_n.is_integer():
        result=pow(sqrt_n+1,2)
    else:
        result=-1
        
    return result