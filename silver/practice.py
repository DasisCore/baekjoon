# 이곳은 문제를 풀며 자유롭게 코드를 짜볼 수 있는 공간입니다.
# 1번 = > n자리 m진수 모두 출력

n, m = map(int, input().split())
arr = []
def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(m):
        arr[cur] = i
        recur(cur + i)
