def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    lq = keypad['*']
    rq = keypad['#']
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            lq=keypad[num]
        elif num in [3,6,9]:
            answer+='R'
            rq=keypad[num]
        else:
            targetnum = keypad[num]
            left_dist = abs(lq[0] - targetnum[0]) + abs(lq[1] - targetnum[1])
            right_dist = abs(rq[0] - targetnum[0]) + abs(rq[1] - targetnum[1])
            if left_dist<right_dist:
                answer+='L'
                lq=targetnum
            elif left_dist>right_dist:
                answer+='R'
                rq=targetnum
            elif left_dist==right_dist:
                if hand=='right':
                    answer+='R'
                    rq=targetnum
                else:
                    answer+='L'
                    lq=targetnum
    return answer