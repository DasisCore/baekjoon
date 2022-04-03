# 11726. 2xn 타일링

# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
#
# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
#
# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

########################################################################################################

# # 탑다운 방식
import sys
sys.setrecursionlimit(1 << 30)

def recur(cur):
    ret = 0

    if cur > n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    if cur == n:
        return 1

    for i in range(1, 3):
        ret += recur(cur + i)

    dp[cur] = ret

    return dp[cur]


n = int(input())
dp = [-1] * (n + 1)
print(recur(0) % 10007)

# 바텀업

n = int(input())
dp = [-1] * (1010)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])