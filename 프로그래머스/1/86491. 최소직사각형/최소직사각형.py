def solution(sizes):
    maxx = 0
    maxy = 0
    for x,y in sizes:
        if x<y:
            x,y=y,x
        maxx = max(maxx,x)
        maxy = max(maxy,y) 
    return maxx*maxy