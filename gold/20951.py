# 20951. 유아와 곰두리차

# 문제
# 유아는 새해를 맞이하여 V.Nets의 자율 주행 자동차를 구매하였다. 유아는 새 차를 타고 바다로 가서 회를 잔뜩 먹고 올 것이다(유아는 감염병 예방을 위한 정부의 방역지침을 준수한다). 고속도로를 달리던 유아는 놀라 자빠질 수밖에 없었다. V.Nets의 자율 주행 시스템이 형편없었기 때문이다. V.Nets에 큰 배신감을 느낀 유아는 직접 자율 주행 자동차를 설계하기로 결심하였다.
# 곰두리차는 유아가 설계한 자율 주행 자동차이다. 곰두리차는 항상 인접한 정점 중 임의의 정점으로 이동한다. 유아는 출발점에서 도착점까지의 경로가 존재하고 시간이 무한하다면 곰두리차가 언제나 목적지에 도달할 수 있다고 믿고 있다. 유아는 문득 그래프가 주어졌을 때, 곰두리차가 지날 수 있는 경로가 몇 개인지 궁금해졌다.
# 하지만 유아는 이 문제를 풀지 못하였다. 문제의 난이도를 낮추기 위하여 유아는 경로상에서 동일한 정점 또는 간선을 재방문하는 것을 허용하였다.
# 그래프가 주어졌을 때, 곰두리차가 지날 수 있는 경로 중 길이가 7인 경로의 개수를 구하는 프로그램을 작성하시오. 곰두리차는 동일한 정점 또는 간선을 여러 번 지날 수 있다.
#
# 입력
# 첫 번째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# 이후 M개의 줄에 걸쳐 간선이 연결하는 두 정점 번호 u, v가 주어진다.
# 주어지는 간선은 양방향 간선이며, 모든 입력은 공백으로 구분되어 주어진다.
#
# 출력
# 첫 번째 줄에 곰두리차가 지날 수 있는 경로 중 길이가 7인 경로의 개수를 출력한다. 답이 매우 커질 수 있으므로 109 + 7로 나눈 나머지를 출력한다.
#
# 제한
# 2 ≤ N ≤ 100,000
# 1 ≤ M ≤ min(N × (N - 1) / 2, 100,000)
# 1 ≤ u, v ≤ N
# u ≠ v
# 입력으로 주어진 그래프에는 중복 간선이 존재하지 않는다.

####################################################################################################

# 탑 다운
import sys
sys.setrecursionlimit(1 << 30)

def recur(cur, cnt):
    ret = 0
    
    # 7칸을 돌아 다녔다면
    if cnt == 7:
        return 1
    
    # 메모이제이션 적용
    if dp[cur][cnt] != -1:
        return dp[cur][cnt]
    
    # 갈 수 있는 간선
    for i in g[cur]:
        # 틈틈히 모듈러를 해줌 // 크기가 너무 커지면 느려지기 때문
        ret += recur(i, cnt + 1) % (10**9 + 7)

    dp[cur][cnt] = ret
    return dp[cur][cnt]


n, m = map(int, sys.stdin.readline().strip().split())
g = [[] for i in range(n + 1)]

# 양방향 간선
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    g[a].append(b)
    g[b].append(a)


total = 0
# 최대 7칸까지만 움직이므로 dp는 8까지 만들어준다.
dp = [[-1] * 8 for i in range(n + 2)]
for i in range(1, n + 1):
    total = (total + recur(i, 0)) % (10**9 + 7)
print(total)