# 11725. 트리의 부모 찾기

# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

#######################################################################################

# 각 노드의 부모이므로, BFS의 특성을 이용해
# BFS로 풀이한다. => 부모 노드를 잘 찾아가지 못함.
# DFS를 이용하여 맨 밑 노드로부터 부모 노드를 찾아가는 방식으로 다시 풀어봄
# 너무 어렵게 생각한 것이 시간을 너무 많이 잡아 먹었다.
# 자식노드에 도착할 때 출발한 것이 부모 노드이므로
# 이 부모 노드를 저장하기만 하면 쉽게 풀리는 문제였다.
from collections import deque
import sys

def DFS(i):
    global visited
    stack.append(i)
    while stack:
        a = stack.pop()
        for i in graph[a]:
            if not visited[i]:
                # 부모 노드를 거쳐서 자식 노드로 가므로,
                # a가 i 노드의 부모가 된다.
                visited[i] = a
                stack.append(i)

n = int(sys.stdin.readline().strip())
graph = [[] for i in range(n + 1)]

# 트리를 양 방향으로 입력 받기
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 사용
stack = deque()
visited = [False] * (n + 1)
DFS(1) # 시작 노드 "1"
for i in range(2, n + 1):
    print(visited[i])
