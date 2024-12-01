
list1=[]
def push(list,x):
    list.append(x)
def pop(list):
    if empty(list):
        print(-1)
    else:
        print(list[-1])
        del list[-1]

def size(list):
    cnt=0
    for i in list:
        cnt+=1
    return cnt
def empty(list):
    leng = size(list)
    if leng==0:
        return 1
    else:
        return 0
def top(list):
    if empty(list):
        print(-1)
    else:
        print(list[-1])


input1 = int(input())
for i in range(input1):
    a = list(input().split())
    if len(a)==2:
        com = a[0]
        num = a[1]
        if com == 'push':
            push(list1,num)
    else:
        com = a[0]
        if com == 'top':
            top(list1)
        elif com == 'size':
            print(size(list1))
        elif com == 'pop':
            pop(list1)
        elif com == 'empty':
            print(empty(list1))
