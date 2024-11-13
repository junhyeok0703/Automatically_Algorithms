a=[int(input()) for _ in range(10)]

sum1=0
result=0
for i in range(10):
    sum1+=a[i]
    if sum1>=100:
        s1 = abs(100-sum1)
        s2 = abs(100-(sum1-a[i]))
        if s1>s2:
            result=sum1-a[i]
        else:
            result=sum1
        break
else:
    result=sum1
print(result)
