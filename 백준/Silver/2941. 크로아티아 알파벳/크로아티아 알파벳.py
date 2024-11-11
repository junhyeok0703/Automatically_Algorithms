
word = input()
cnt = 0
i = 0

while i < len(word):
    if i < len(word) - 1 and word[i] == 'c' and word[i + 1] == '=':
        cnt += 1
        i += 2
    elif i < len(word) - 1 and word[i] == 'c' and word[i + 1] == '-':
        cnt += 1
        i += 2
    elif i < len(word) - 2 and word[i] == 'd' and word[i + 1] == 'z' and word[i + 2] == '=':
        cnt += 1
        i += 3
    elif i < len(word) - 1 and word[i] == 'd' and word[i + 1] == '-':
        cnt += 1
        i += 2
    elif i < len(word) - 1 and word[i] == 'l' and word[i + 1] == 'j':
        cnt += 1
        i += 2
    elif i < len(word) - 1 and word[i] == 'n' and word[i + 1] == 'j':
        cnt += 1
        i += 2
    elif i < len(word) - 1 and word[i] == 's' and word[i + 1] == '=':
        cnt += 1
        i += 2
    elif i < len(word) - 1 and word[i] == 'z' and word[i + 1] == '=':
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)