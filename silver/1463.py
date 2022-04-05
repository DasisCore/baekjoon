# 1463. 1로 만들기

# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
#
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

########################################################################################

import sys
sys.setrecursionlimit(1 << 30)

def recur(cur):
    if cur == 1:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = recur(cur - 1) + 1

    if not cur % 3:
        dp[cur] = min(dp[cur], recur(cur // 3) + 1)

    if not cur % 2:
        dp[cur] = min(dp[cur], recur(cur // 2) + 1)

    return dp[cur]


n = int(input())
dp = [-1] * 1000010
print(recur(n))

##################################################################

n = int(input())
dp = [10000] * (1000010)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2

if n > 3:
    for i in range(4, n + 1):

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[n])