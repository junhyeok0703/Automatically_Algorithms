n = int(input())
wordlist = []
set(wordlist)
for i in range(n):
    word = input()
    if word not in wordlist:
        wordlist.append(word)

wordlist.sort(key=lambda x: (len(x),x))

for i in wordlist:
    print(i)