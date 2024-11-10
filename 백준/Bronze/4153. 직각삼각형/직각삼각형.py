aa=[]
while True:
    a,b,c = map(int, input().split())
    rr = ([a,b,c])
    rr.sort()
    if rr[0]==0 and rr[1]==0 and rr[2]==0:
        break
    if (rr[0]*rr[0])+(rr[1]*rr[1])==(rr[2]*rr[2]):
        aa.append('right')
    else:
        aa.append('wrong')

for i in aa:
    print(i)