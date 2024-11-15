n,x,k = map(int,input().split())

# k 수행 위치바꾸기
# x 번째 공이 있다
arr1= [0]*(n+1)
arr1[x]=1
for i in range(k):
    a,b = map(int,input().split())
    arr1[a],arr1[b]=arr1[b],arr1[a]

print(arr1.index(1))