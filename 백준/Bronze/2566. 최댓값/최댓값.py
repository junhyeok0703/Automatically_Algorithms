maplist=[]
for i in range(9):
    maplist.append(list(map(int,input().split())))
m1=[]
for i in range(9):
    m1.append(max(maplist[i]))

myf = max(m1)
print(myf)
for i in range(9):
    for j in range(9):
        if myf==maplist[i][j]:
            print(i+1,j+1)
            break
