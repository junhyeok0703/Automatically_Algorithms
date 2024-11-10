def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
count = 0
last = factorial(n)
last = list(str(last))
last = reversed(last)

for i in last:
    if i == '0':
        count += 1
    else:
        print(count)
        break

