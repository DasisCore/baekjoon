# 18111. 마인크래프트

import sys

n, m, b = map(int, sys.stdin.readline().split(" "))

space = []
s = 0
for i in range(n): # 입력된 땅의 높낮이를 2차원 리스트로 형성
    coo = list(map(int, sys.stdin.readline().split(" ")))
    space.append(coo)
    s += sum(coo)

# 여기서의 i값은 땅의 높이임.
answer = [] #완전탐색, 각 높이에 대한 결과값이 저장될 곳
for high in range(0, 257): #전체 높이
    time = 0 # 각 높이의 회차 마다 초기화 시켜줌
    block = b
    for i in space:
        for j in i:
            if j == high:
                pass
            elif j < high: #블록 쌓기
                di = abs(j - high)
                time += di * 1
                block -= di * 1
            else: # 땅 파고 인벤토리
                di = abs(j - high) # 땅을 파고 인벤토리에 넣는 시간
                time += di*2 
                block += di * 1
    if block < 0: #블록이 모자랄 경우 break
        break
    else:
        answer.append((time, high))

answer.sort(key= lambda x : (x[0], -x[1])) 
#  x[0]을 기준으로 정렬, 이후 값이 같을 경우 x[1]의 내림차순
print(*answer[0]) #언팩