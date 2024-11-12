n , m = map(int,input().split())
arr1 = list(map(int,input().split()))
max1 = 0
cnt1=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = arr1[i]+arr1[j]+arr1[k]
            cnt1+=1
            if m>=a:
                max1= max(a,max1)

print(max1)