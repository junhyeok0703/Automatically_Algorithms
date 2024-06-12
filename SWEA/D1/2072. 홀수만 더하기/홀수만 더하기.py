
T = int(input())


sums = []


for test_case in range(1, T + 1):
 
    numbers = list(map(int, input().split()))

    odd_sum = sum(num for num in numbers if num % 2 == 1)
    
 
    sums.append(odd_sum)


for i in range(T):
    print("#{} {}".format(i + 1, sums[i]))
