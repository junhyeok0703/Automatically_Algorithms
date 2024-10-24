import math
def solution(numer1, denom1, numer2, denom2):
    b = denom1*denom2
    a = numer1*denom2 + numer2*denom1
    c = math.gcd(a,b)
    a//=c
    b//=c
    return [a,b]