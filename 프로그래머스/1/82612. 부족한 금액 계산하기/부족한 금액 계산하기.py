def solution(price, money, count):
    total_cost = 0
    for i in range(1, count + 1):
        total_cost += price * i
    
    remaining_money = money - total_cost
    if remaining_money < 0:
        return -remaining_money
    else:
        return 0
