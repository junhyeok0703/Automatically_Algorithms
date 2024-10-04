n,m = map(int,input().split())
alist = [0]*(n+1)
for i in range(m):
    i,j,k= map(int,input().split())
    for a in range(i,j+1):
        alist[a]=k


print(' '.join(map(str,alist[1:])))