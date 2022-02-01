# 18111. 마인크래프트

import sys

n, m, b = map(int, sys.stdin.readline().split(" "))

space = []
s = 0
for i in range(n): # 입력된 땅의 높낮이를 2차원 리스트로 형성
    coo = list(map(int, sys.stdin.readline().split(" ")))
    space.append(coo)
    s += sum(coo)

#만들어야할 땅의 높이.
aver = round(s/(n*m))

block = s - aver*(n*m) + b
while True:
    if block < 0:
        aver -= 1
        break
    else:
        break


time = 0
answer = []
for i in space:
    for j in i:
        if j == aver:
            pass
        elif j < aver: # 블록을 쌓는 시간
            di = abs(j - aver)
            time += di * 1
            b -= di * 1
        elif j > aver:
            di = abs(j - aver) # 땅을 파고 인벤토리에 넣는 시간
            time += di*2 
            b += di * 1
else:
    answer.append((time, aver))

time = 0
for i in space:
    for j in i:
        if j == aver+1:
            pass
        elif j < aver+1: # 블록을 쌓는 시간
            di = abs(j - aver+1)
            time += di * 1
            b -= di * 1
        elif j > aver+1:
            di = abs(j - aver+1) # 땅을 파고 인벤토리에 넣는 시간
            time += di*2 
            b += di * 1
else:
    answer.append((time, aver+1))

answer.sort(key= lambda x : x[1], reverse = True)
if answer[0][0] == answer[1][0]:
    print(*answer[0])
else:
    print(*answer[1])

