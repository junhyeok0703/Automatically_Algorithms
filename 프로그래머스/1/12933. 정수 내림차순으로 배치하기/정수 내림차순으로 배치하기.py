def solution(n):
    arr = []
    numstring = str(n)
    for num in numstring:
        arr.append(int(num))
    a = sorted(arr,reverse=True)
    leng = len(a)
    sum=0
    for i in range(len(a)):
        mul = pow(10,leng-i-1)
        sum+=a[i]*mul
    return sum