# 15681. 트리와 쿼리

# 문제
# 간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
# 만약 이 문제를 해결하는 데에 어려움이 있다면, 하단의 힌트에 첨부한 문서를 참고하자.
#
# 입력
# 트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)
# 이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)
# 이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.
# 이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)
# 입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.
#
# 출력
# Q줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력한다.

########################################################################################

import sys
sys.setrecursionlimit(1 << 30)

# 트리의 부모찾기 베이스
def dfs(cur, prv):
    # 자기 자신의 size는 일단 1을 갖는다.
    sz[cur] = 1

    for nxt in li[cur]:
        # 앞으로 갈 곳이 이전에 갔던 곳이라면 가지 않음.
        if nxt == prv:
            continue
        # sz의 크기는 서브트리의 크기가 된다.
        sz[cur] += dfs(nxt, cur)

    # dp의 탑다운을 생각하면 편함.
    return sz[cur]

# 기본값들 입력받기
n, r, q = map(int, sys.stdin.readline().strip().split())

# 방향성이 없는 트리 생성
li = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    li[a].append(b)
    li[b].append(a)

# dp를 위해 각 서브트리의 사이즈를 기록할 sz 리스트
sz = [0 for i in range(n + 1)]

# 루트트리를 기준으로 dfs
dfs(r, -1)

# 주어지는 각 쿼리에 따라 size를 출력한다.
for i in range(q):
    u = int(sys.stdin.readline().strip())
    print(sz[u])