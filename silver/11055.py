# 11055. 가장 큰 증가 부분 수열

# 문제
# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

####################################################################################

import sys
sys.setrecursionlimit(1 << 30)

def recur(cur, prv):

    if cur == n:
        return 0

    if dp[cur][prv] != -1:
        return dp[cur][prv]

    # 이전에 보고 있던 수가, 지금 보는 수보다 작다면
    if li[cur] > li[prv]:
        # 그 수를 더하는 것과 그냥 넘어가는 것중 큰 값을 ret에 넣는다
        ret = max(recur(cur + 1, cur) + li[cur], recur(cur + 1, prv))
    # 이전에 보고 있던 수가 지금보는 수보다 크다면 넘어간다
    else:
        ret = recur(cur + 1, prv)
    
    # 메모이제이션
    dp[cur][prv] = ret

    return dp[cur][prv]

n = int(input())
li = list(map(int, input().split())) + [0]
dp = [[-1] * 1010 for i in range(1010)]
print(recur(0, n))