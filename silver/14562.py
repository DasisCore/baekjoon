# 14562. 태권왕

# 문제
# 태균이는 지금 태권도 겨루기 중이다. 지금은 상대에게 지고 있지만 지금부터 진심으로 경기하여 빠르게 역전을 노리려 한다.
# 태균이가 현재 할 수 있는 연속 발차기는 두가지가 있다.
# A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
# B는 1점을 얻는 연속 발차기이다.
# 현재 태균이의 점수 S와 상대의 점수 T가 주어질 때, S와 T가 같아지는 최소 연속 발차기 횟수를 구하는 프로그램을 만드시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 수 C(1 ≤ C ≤ 100)이 주어진다. 둘째 줄부터 C줄에 걸쳐 테스트 케이스별로 현재 점수 S와 T가 공백을 사이에 두고 주어진다. (1 ≤ S < T ≤ 100)
#
# 출력
# 각 줄마다 S와 T가 같아지는 최소 연속 발차기 횟수를 출력한다.

############################################################################################################

# 1. 백트래킹 풀이
def recur(s, t, cnt):
    global answer
    # 불필요한 재귀를 차단
    if s < t + 1:
        # 정답 요건에 도달했을 때, 최소값으로 정답갱신
        if s == t:
            answer = min(answer, cnt)
            return

        # 엄청난 연속 발차기
        recur(s + s, t + 3, cnt + 1)
        # 1점을 얻는 연속 발차기
        recur(s + 1, t, cnt + 1)


c = int(input())
for _ in range(c):
    # s와 t가 같아지는 최소 횟수를 구해야 하므로.
    # 백트래킹이 먼저 생각남.
    answer = 99999
    s, t = map(int, input().split())
    recur(s, t, 0)
    print(answer)

# 2. BFS풀이

# BFS로 풀이를 진행할 예정이므로 deque 사용
from collections import deque

def BFS():
    queue.append([s, t, 0])
    answer = 9999999

    while queue:
        a, b, c = queue.popleft()
        # 무한루프에 빠지는 것을 막기 위해
        # 밑의 조건이 없다면 a가 b를 넘어섰을때 멈추지 못하고
        # 계속 계산이 진행되므로 메모리 초과가 나게 된다.
        if a < b + 1:
            if a == b:
                answer = min(answer, c)
                return answer

            queue.append([a + a, b + 3, c + 1])
            queue.append([a + 1, b, c + 1])

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    queue = deque()
    print(BFS())
