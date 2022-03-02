# 11724. 연결 요소의 개수

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
#
# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

###################################################################################################################

# 방향 없는 그래프
def DFS(Z):
    global g, visited
    stack = [Z] # 시작 노드
    while stack:
        Z = stack.pop()
        visited[Z] = 1
        for i in range(1, n + 1):
            # 시작 노드를 기준으로 연결된 노드들을 방문하며 체크함
            if g[Z][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(i)



n, m = map(int, input().split())

# 인접 행렬 사용
g = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    o, k = map(int, input().split())
    g[o][k], g[k][o] = 1, 1
visited = [0 for i in range(n + 1)] #노드의 개수

# 연결 요소의 개수
cnt = 0
# 연결되지 않은 노드가 있더라도 요소의 개수에는 해당되므로.
# for문을 이용하여 갯수를 세어준다.
for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        DFS(i)

print(cnt)
