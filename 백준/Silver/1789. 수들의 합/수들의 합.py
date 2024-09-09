sum =0
S = int(input())
i=1
count=0
while sum+i<=S:
    sum+=i
    count+=1
    i+=1
print(count)