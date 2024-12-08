
class Q:
    def __init__(self):
        self.queue=[]
    def push(self,x):
        self.queue.append(int(x))
    def pop(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return -1
    def size(self):
        cnt=0
        for i in self.queue:
            cnt+=1
        return cnt
    def empty(self):
        return 1 if self.size()==0 else 0
    def front(self):
        if not self.empty():
            return self.queue[0]
        else:
            return -1

    def back(self):
        if not self.empty():
            return self.queue[-1]
        else:
            return -1
q = Q()
input1 = int(input())
for i in range(input1):
    a = list(input().split())
    if len(a)==2:
        com = a[0]
        num = a[1]
        if com == 'push':
            q.push(num)
    else:
        com = a[0]
        if com == 'front':
            print(q.front())
        elif com == 'size':
            print(q.size())
        elif com == 'pop':
            print(q.pop())
        elif com == 'empty':
            print(q.empty())
        elif com == 'back':
            print(q.back())