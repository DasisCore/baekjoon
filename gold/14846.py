# 14846. 직사각형과 쿼리

# 문제
# N행 N열로 이루어진 정사각형 행렬 A가 주어진다. 이때, 쿼리를 수행하는 프로그램을 작성하시오.
# x1 y1 x2 y2: 왼쪽 윗칸이 (x1, y1)이고, 오른쪽 아랫칸이 (x2, y2)인 부분 행렬에 포함되어 있는 서로 다른 정수의 개수를 출력한다.
#
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 300)이 주어진다. 다음 N개의 줄에는 행렬의 정보가 주어지며, 각 줄은 N개의 수로 이루어져 있다. 행은 위에서부터 아래로, 열은 왼쪽부터 오른쪽으로 번호가 매겨져 있으며, 번호는 1번부터 시작한다. 행렬이 포함하고 있는 정수는 10보다 작거나 같은 자연수이다.
# 다음 줄에는 Q (1 ≤ Q ≤ 100,000)가 주어진다. 다음 Q개의 줄에는 쿼리의 정보 x1, y1, x2, y2가 주어진다. (1 ≤ x1 ≤ x2 ≤ n, 1 ≤ y1 ≤ y2 ≤ n)
#
# 출력
# 각각의 쿼리마다 정답을 한 줄에 하나씩 출력한다.

####################################################################################################################

import sys, copy

n = int(sys.stdin.readline())
a = [[0] + list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
li = [[[0] * (n + 1)] + copy.deepcopy(a) for j in range(11)]
prefix = [[[0] * (n + 1) for i in range(n + 1)] for j in range(11)]

for k in range(1, 11):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if li[k][i][j] == k:
                prefix[k][i][j] = prefix[k][i - 1][j] + prefix[k][i][j - 1] - prefix[k][i - 1][j - 1] + li[k][i][j]
            else:
                li[k][i][j] = 0
                prefix[k][i][j] = prefix[k][i - 1][j] + prefix[k][i][j - 1] - prefix[k][i - 1][j - 1] + li[k][i][j]

q = int(sys.stdin.readline())
for j in range(q):
    cnt = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(1, 11):
        a = prefix[i][x2][y2] - prefix[i][x1 - 1][y2] - prefix[i][x2][y1 - 1] + prefix[i][x1 - 1][y1 - 1]
        if a:
            cnt += 1
    print(cnt)