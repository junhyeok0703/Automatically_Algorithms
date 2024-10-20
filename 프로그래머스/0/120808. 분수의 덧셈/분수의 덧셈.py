import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    d = denom1 * denom2
    n1 = numer1*denom2
    n2 = numer2*denom1
    n3 = n1+n2
    gcd = math.gcd(n3,d)
    if gcd>0:
        a = n3//gcd
        b = d//gcd
    return [a,b]