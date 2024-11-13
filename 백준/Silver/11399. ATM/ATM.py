n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
sum1=0
result=0
for i in range(len(arr1)):
    sum1+=arr1[i]
    result+=sum1
print(result)