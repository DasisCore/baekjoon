# 11727. 2 x n 타일링 2

# 문제
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.
#
# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
#
# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

############################################################################


# import sys
# sys.setrecursionlimit(1 << 30)
#
# def recur(cur):
#     ret = 0
#     if cur > n:
#         return 0
#
#     if dp[cur] != -1:
#         return dp[cur]
#
#     if cur == n:
#         return 1
#
#     for i in range(1, 3):
#         ret += recur(cur + i) * i
#
#     dp[cur] = ret
#     return dp[cur]
#
# n = int(input())
# dp = [-1] * 1010
# print(recur(0) % 10007)


n = int(input())
dp = [-1] * 1010
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
print(dp[n] % 10007)

