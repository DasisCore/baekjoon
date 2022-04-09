# 5525. IOIOI

# 문제
# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.
#
# 출력
# S에 PN이 몇 군데 포함되어 있는지 출력한다.
#
# 제한
# 1 ≤ N ≤ 1,000,000
# 2N+1 ≤ M ≤ 1,000,000
# S는 I와 O로만 이루어져 있다.

########################################################################################################################

# 앞에서부터 빼기 위해 deque를 사용했다.
from collections import deque

n = int(input())
m = int(input())
string = deque(input())

# i와 o의 개수를 세기 위함.
i = 0
o = 0

# 이전 문자인 prv를 체크해주기 위해 하나만 먼저 뺐다.
prv = string.popleft()
if prv == "I":
    i += 1
else:
    o += 1

# Pn을 세주기 위한 cnt
cnt = 0
while string:
    check = string.popleft()
    
    if prv == check == "I":
        cnt += max(i - n, 0)
        i = 1
        o = 0
    elif prv == check == "O":
        cnt += max(i - n, 0)
        i = 0
        o = 0
    elif prv == "I" and check == "O":
        o += 1
    elif prv == "O" and check == "I":
        i += 1
    prv = check

# 정확한 IOIO....IOI로 끝날 가능성이 있기 때문에
cnt += max(i - n, 0)
print(cnt)
