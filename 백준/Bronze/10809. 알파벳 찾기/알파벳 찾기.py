str1 = input()
result = [-1] * 26
for i in range(len(str1)):
    index = ord(str1[i]) - ord('a')
    if result[index] == -1:
        result[index] = i

print(' '.join(map(str, result)))