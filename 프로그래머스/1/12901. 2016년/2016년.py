def solution(a, b):
    day_week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    
    total_days = sum(days_in_month[:a-1]) + (b - 1)
    
    return day_week[(total_days + 5) % 7]