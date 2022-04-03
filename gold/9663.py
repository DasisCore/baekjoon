# 9663. N-Queen

# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

######################################################################

# def recur(cur):
#     global cnt
#
#     if cur == n:
#         cnt += 1
#         return
#
#     for i in range(n):
#         if visited[cur][i]:
#             continue
#
#         # 방문처리
#         for j in range(n - cur):
#             for k in range(6):
#                 x = cur + di[k] * j
#                 y = i + dj[k] * j
#                 if -1 < x < n and -1 < y < n:
#                     visited[x][y] += 1
#
#         recur(cur + 1)
#
#         # 방문처리 초기화
#         for j in range(n - cur):
#             for k in range(6):
#                 x = cur + di[k] * j
#                 y = i + dj[k] * j
#                 if -1 < x < n and -1 < y < n:
#                     visited[x][y] -= 1
#
# n = int(input())
# visited = [[0] * n for i in range(n)]
#
# # 밑으로만 내려가므로 6방 탐색
# di = [-1, 1, 0, 0, 1, 1]
# dj = [0, 0, -1, 1, -1, 1]
#
# cnt = 0
# recur(0)
# print(cnt)



def check(cur):
    for i in range(cur):
        if abs(row[cur] - row[i]) == cur - i:
            return False
    return True

def recur(cur):
    global cnt

    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        row[cur] = i
        if check(cur):
            visited[i] = 1
            recur(cur + 1)
            visited[i] = 0


n = int(input())
row = [0] * n
visited = [0] * n
cnt = 0
recur(0)
print(cnt)