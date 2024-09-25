n,k= list(map(int,input().split()))
dong = []
for i in range(n):
    dong.append(int(input()))
dongcnt=0
dong.sort(reverse=True)
for i in dong:
    if k<i:
        continue
    dongcnt += k//i
    k%=i

print(dongcnt)