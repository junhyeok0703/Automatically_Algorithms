def solution(phone_number):
    length = len(phone_number)
    hibbenarr = "*" * (length-4)
    copyarr = phone_number[-4:]
    return hibbenarr+copyarr