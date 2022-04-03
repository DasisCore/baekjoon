# 15988. 1, 2, 3 더하기 3

# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 1,000,000보다 작거나 같다.
#
# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.

####################################################################################

import sys
sys.setrecursionlimit(1 << 30)

def recur(total):
    ret = 0

    if total < 0:
        return 0

    if total == 0:
        return 1

    if dp[total] != -1:
        return dp[total]

    for i in range(1, 4):
        ret += recur(total - i)

    dp[total] = ret

    return dp[total]

t = int(sys.stdin.readline())
dp = [-1] * 1000001
for _ in range(t):
    n = int(sys.stdin.readline())
    print(recur(n) % 1000000009)

############################################################################################################

import sys

n = int(sys.stdin.readline().strip())
dp = [0] * 1000001
dp[0] = 1; dp[1] = 1; dp[2] = 2

for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

for _ in range(n):
    m = int(sys.stdin.readline().strip())
    print(dp[m] % 1000000009)

