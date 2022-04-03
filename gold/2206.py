# 2206. 벽 부수고 이동하기

# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
#
# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

###########################################################################################

from collections import deque

# 코드가 맵 안에서 놀도록 제한
def in_range(x, y):
    return -1 < x < n and -1 < y < m

# 최단거리이므로 BFS 활용
def bfs(a, b, c):
    global ans
    
    # 벽을 부수었나 안부수었나를 확인하기 위한 3차원 리스트
    visited = [[[0] * 2 for i in range(m)] for j in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    queue = deque()
    queue.append([a, b, c])

    d = 1
    while queue:
        # size는 이동 거리를 체크하기 위함임. (깊이를 계산)
        size = len(queue)
        for _ in range(size):
            a, b, c = queue.popleft()
            
            # n, m의 위치에 도달했다면, 최단 경로를 출력하고 종료
            if a == n - 1 and b == m - 1:
                print(d)
                exit()
            
            # 델타이동
            for i in range(4):
                x = a + di[i]
                y = b + dj[i]
                if not in_range(x, y):
                    continue

                # 만약 벽을 부수었다면 nc라는 변수를 만들어 체크해준다.
                nc = c + int(g[x][y])

                # 벽을 2번 이상 부쉈거나, 이미 방문한 곳이라면 continue
                if nc > 1 or visited[x][y][nc]:
                    continue

                # 벽의 파괴 유무를 기준으로 나누어 bfs를 한다.
                queue.append([x, y, nc])
                visited[x][y][nc] = 1
        d += 1




n, m = map(int, input().split())
g = [input() for i in range(n)]
ans = -1
# 0, 0에서 출발, 3번째 인자는 벽을 부수었나 안부수었나를 의미
bfs(0, 0, 0)
print(ans)
