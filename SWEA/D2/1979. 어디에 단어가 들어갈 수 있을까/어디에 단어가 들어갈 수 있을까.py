# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
result=[]
def countfun(puzzle,wordlen):
    # 가로만 보기
    cnt1 = 0
    result = 0
    for row in puzzle:
        cnt1 = 0
        for i in row:
            if i == 0:
                if cnt1==wordlen: # 0이 됬을때 1을 세는게 끝난거니까 0까지 1나온거 센거보고 wordlen이랑 같으면 하나 추가 또 이제 cnt1은 0으로 다시시작
                    result+=1
                cnt1=0
            elif i == 1: # 1이면 cnt올려
                cnt1+=1
        if cnt1==wordlen: # 만약 남은 cnt1이 wordlen이 같으면 하나 올려 0 0 1 1 1같은 경우가 있음
            result+=1

    # 세로만 보기
    cnt2 = 0
    for j in range(len(puzzle)):
        cnt2 = 0
        for i in range(len(puzzle)):
            if puzzle[i][j] == 0:# 세로로 이동
                if cnt2==wordlen:
                    result+=1
                cnt2=0
            elif puzzle[i][j]==1:
                cnt2+=1
        if cnt2==wordlen:
            result+=1

    return result

rrarr=[]
for i in range(1,T+1):
    a,b = map(int,input().split())
    resultarr= []
    for i in range(a):
        resultarr.append(list(map(int,input().split())))
    rrarr.append(countfun(resultarr,b))
for i in range(len(rrarr)):
    print(f'#{i+1} {rrarr[i]}')