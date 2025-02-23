def solution(N, number):
    dp = [[] for _ in range(9)]
    
    for i in range(1, 9):
        current_set = set()
        current_set.add(int(str(N) * i))
        for j in range(1, i):
            for num1 in dp[i - j]:
                for num2 in dp[j]:
                    current_set.add(num1 + num2)
                    current_set.add(num1 - num2)
                    current_set.add(num1 * num2)
                    if num2 != 0 and num1 % num2 == 0:
                        current_set.add(num1 // num2)
        if number in current_set:
            return i
        dp[i] = list(current_set)
    
    return -1
