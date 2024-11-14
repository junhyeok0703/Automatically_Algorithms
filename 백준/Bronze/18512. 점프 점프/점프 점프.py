x,y,p1,p2= map(int,input().split())
p1arr=set()
p2arr=set()
result =-1
for i in range(100):
    pos_a= p1+i*x
    pos_b = p2+i*y


    p1arr.add(pos_a)
    p2arr.add(pos_b)

    if pos_a in p2arr:
        result = pos_a
        break
    elif  pos_b in p1arr:
        result = pos_b
        break

if result==-1:
    print(-1)
else:
    print(result)