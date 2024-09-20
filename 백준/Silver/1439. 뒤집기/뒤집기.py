import math

S = list(map(int,input()))
stack = []
check = S[0]
cnt=0
for i in S:
    if check!=i:
        cnt+=1
        check=i

print(math.ceil(cnt/2))
