# 11053. 가장 긴 증가하는 부분 수열

# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

############################################################################

import sys
sys.setrecursionlimit(1 << 30)

n = int(input())
li = list(map(int, input().split())) + [0]
dp = [[-1] * (1010) for i in range(1010)]

def recur(cur, prv):
    if cur == n:
        return 0

    if dp[cur][prv] != -1:
        return dp[cur][prv]
    
    # 지금 보고 있는 수가 저번 수보다 크다면
    if li[cur] > li[prv]:
        # 고르는 것과 안고르는 것 중 max
        ret = max(recur(cur + 1, cur) + 1, recur(cur + 1, prv))
    else:
        # 작으면 그냥 넘어가기
        ret = recur(cur + 1, prv)

    dp[cur][prv] = ret

    return dp[cur][prv]

print(recur(0, n))