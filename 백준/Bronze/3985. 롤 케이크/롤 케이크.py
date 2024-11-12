m = int(input())
pcnt = int(input())
max1 = 0
ind = -1
arr1 = [0]*m
realmax=0
realind = 0
for i in range(1,pcnt+1):
    a,b = map(int,input().split())
    if max1<b-a:

        ind = i
        max1=b-a
    cnt1=0
    for j in range(a,min(b+1,m)):
        if arr1[j]!=1:
            arr1[j]=1
            cnt1+=1
        if realmax<cnt1:
            realmax=cnt1
            realind =i
print(ind)
print(realind)