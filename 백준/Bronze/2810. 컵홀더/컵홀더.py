n = int(input())
arr1= list(input())
cnt1=0
for i in range(len(arr1)):
    if arr1[i]=='L':
        cnt1+=1


result = (((n-cnt1)+cnt1//2)+1)

if n<result:
    print(n)
else:
    print(result)