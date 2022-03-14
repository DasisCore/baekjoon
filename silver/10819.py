# 10819. 차이를 최대로

# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
#
# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

####################################################################################################

def recur(cur):
    global answer

    # arr가 완성되었을 때
    if cur == n:
        total = 0
        # 문제에서 주어진 식을 실행
        for i in range(1, n):
            total += abs(arr[i] - arr[i - 1])

        # 최댓값으로 정답 갱신
        answer = max(answer, total)
        return

    # 중복이 없는 배열 만들기
    for i in range(n):
        if visited[i]:
            continue

        arr[cur] = li[i]
        visited[i] = 1
        recur(cur + 1)
        visited[i] = 0


n = int(input())
li = list(map(int, input().split()))
arr = [0] * n
visited = [0] * n
answer = -99999
recur(0)
print(answer)