# 1074. Z

# 문제
# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
# 다음은 N=3일 때의 예이다.
#
# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.
#
# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

#########################################################################################################

def recur(a, b, num):
    global cnt

    di = [-1, -1, 0, 0]
    dj = [-1, 0, -1, 0]

    if a - num <= r < a and b - num <= c < b:
        if num == 2:
            for i in range(4):
                x = (a - 1) + di[i]
                y = (b - 1) + dj[i]
                if x == r and y == c:
                    print(cnt)
                    return
                cnt += 1
            else:
                return
    else:
        cnt += num * num
        return

    if num > 2:
        cut = num // 2
        recur(a - cut, b - cut, cut)
        recur(a - cut, b, cut)
        recur(a, b - cut, cut)
        recur(a, b, cut)

n, r, c = map(int, input().split())
cnt = 0
recur(2**n, 2**n, 2**n)