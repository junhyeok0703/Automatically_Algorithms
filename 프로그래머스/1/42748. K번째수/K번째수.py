def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        choice = command[2]
        sclice_arr = array[start:end]
        sorted_arr = sorted(sclice_arr)
        answer.append(sorted_arr[choice-1])
    return answer