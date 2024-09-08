N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    booksW = list(map(int, input().split()))
    cnt = 0
    boxcnt = 0
    for i in range(N):
        if cnt + booksW[i] <= M:
            cnt += booksW[i]
        else:
            boxcnt += 1
            cnt = booksW[i]
    if cnt > 0:
        boxcnt += 1
    print(boxcnt)
