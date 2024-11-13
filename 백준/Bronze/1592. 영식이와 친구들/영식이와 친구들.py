n,m,l= map(int,input().split())
arr1=[0]*(n+1)

arr1[1] = 1
i=1
cnt1=0
while True:
    if arr1[i]%2==1 and arr1[i]<m:

        i+=l

        if i>n:
            i-=n


        arr1[i]+=1
        cnt1+=1

    elif arr1[i]%2==0 and arr1[i]<m:
        i -= l

        if i<1:

            i+=n

        arr1[i]+=1
        cnt1+=1


    if m in arr1:
        print(cnt1)
        break
