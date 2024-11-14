n = int(input())
cnt1=0
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j<=n:
            cnt1+=1
print(cnt1)