n = list(input())
n.sort(reverse=True)
a = int(''.join(n))
if a%30==0:
    print(a)
else:
    print(-1)

