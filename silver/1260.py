# 1260. DFS와 BFS

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


#############################################################################

def DFS(v): # v 시작 정점.
    global visited_DFS

    stack = [v] # DFS이므로 queue 사용
    while stack:
        v = stack.pop()
        if not visited_DFS[v]:
            visited_DFS[v] = 1
            print(v, end=" ")
            for j in range(1, n + 1)[::-1]: # 정점번호가 작은 것부터 출력
                if g[v][j] == 1 and not visited_DFS[j]:
                    stack.append(j)


#############################################################################

def BFS(v):
    global visited_BFS

    queue = [v] # BFS이므로 queue 사용
    while queue:
        v = queue.pop(0)
        if not visited_BFS[v]:
            visited_BFS[v] = 1
            print(v, end=" ")
            for j in range(1, n + 1):
                if g[v][j] == 1 and not visited_BFS[j]:
                    queue.append(j)

#############################################################################

n, m, v = map(int, input().split())
# 인접행렬 리스트를 이용해서 풀어보자.

g = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b], g[b][a] = 1, 1 # 양방향 간선이므로.

visited_DFS = [False for i in range(n + 1)]
visited_BFS = [False for i in range(n + 1)]
DFS(v)
print()
BFS(v)












