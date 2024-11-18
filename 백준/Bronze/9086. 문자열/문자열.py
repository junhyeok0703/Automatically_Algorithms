n = int(input())

str2=[]
for i in range(n):
    str1 = input()
    str2.append(str1[0] + str1[-1])

for i in range(n):
    print(str2[i])