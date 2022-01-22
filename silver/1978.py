# 1978. 소수찾기


import sys

def prime(a):
    if a == 1: #1은 소수가 아니다
        return 0
    else:
        for i in range(2, a): #1과 자신을 제외한 수를 돌며 
            if a % i == 0:  #나머지가 0이면 소수가 아니므로
                return 0
        return 1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))

cnt = 0
for i in a:
    cnt += prime(i) #소수임이 판별되면 숫자세기

print(cnt)
