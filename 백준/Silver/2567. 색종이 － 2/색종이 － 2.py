n =int(input())

sarr = [[0]*101 for _ in range(101)]
for i in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            sarr[i][j]=1
cnt1=0
for k in range(101):
    for q in range(101):
        if sarr[k][q]==1:
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                if sarr[k+x][q+y]==0:
                    cnt1+=1
print(cnt1)