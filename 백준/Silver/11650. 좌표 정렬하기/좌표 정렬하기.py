import sys
N = int(sys.stdin.readline())

twolist = []
for i in range(N):
    twolist.append(list(map(int,sys.stdin.readline().split())))


twolist.sort()

for i in range(N):
    print(twolist[i][0],twolist[i][1])
