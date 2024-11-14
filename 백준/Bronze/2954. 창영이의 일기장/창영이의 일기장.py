list1  = input()
result=[]
i=0
vowels = 'aeiou'
while i<len(list1):
    result.append(list1[i])
    if list1[i] in vowels:
        i+=3
    else:
        i+=1

print(''.join(result))