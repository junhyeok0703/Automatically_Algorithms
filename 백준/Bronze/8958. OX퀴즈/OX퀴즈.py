n = int(input())
sarr=[]
for i in range(n):
    cnt1=0
    result=0
    tc1 = list(input())
    for k in range(len(tc1)):
   
        if tc1[k]=='O':
            cnt1+=1
            result+=cnt1
        elif tc1[k]=='X':
            cnt1=0
            result+=cnt1
    sarr.append(result)

for i in sarr:
    print(i)