money = int(input())


result = money // 5
remainder = money % 5

while remainder % 2 != 0:

    result -= 1
    remainder += 5
    if result < 0: 
        print(-1)
        break
else:
   
    result += remainder // 2
    print(result)
