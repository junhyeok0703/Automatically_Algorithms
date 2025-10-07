def answer_arr(arr,n):
    temp=""
    answer = []
    for i in arr:
        bin_i = bin(i)[2:]
        # print(bin_i)
        if len(bin_i) < n:
            diff = n-len(bin_i)
            for j in range(diff):
                temp = temp + "0"
            answer.append(temp + str(bin_i))
            temp=""
        else:
            answer.append(str(bin_i))
    return answer

def diff_arr(arr1,arr2):
    answer_arr = []
    temp = ""
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                temp = temp +"#"
            else: 
                temp = temp + " "
        answer_arr.append(temp)
        temp = ""
    return answer_arr
def solution(n, arr1, arr2):
    # 1. n 길이의 배열을 만들자.
    # 2. arr1,arr2의 배열을 보고 이진수로 배열을 만들자 
    #   2-1. 배열의 하나의 요소를 보면 9(십진수)일 경우에 -> 그걸 이진수로 바꾸자
    #   2-2. 
    # 3. 두 배열을 비교하면서 둘 다 겹치면 #으로 채워서 마지막 배열을 만들자
    # 4. 마지막 배열을 한줄씩 문자열로 출력하자.
    
    ar1 = answer_arr(arr1,n)
    ar2 = answer_arr(arr2,n)
    # print("ar1",ar1)
    # print("ar2",ar2)
    answer= []
    answer = diff_arr(ar1,ar2)
    return answer


