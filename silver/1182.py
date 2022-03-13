# 1182. 부분수열의 합

# 문제
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

################################################################################################

# def recur(cur, start, a):
#     global cnt
#
#     # 목표로 하는 n개의 부분수열에 도달했을 때
#     if cur == a:
#         # 원소를 다 더한 값이 s가 되면 cnt +1
#         if sum(arr) == s:
#             cnt += 1
#         return
#
#     # 중복이 생기지 않는 부분수열 만들기
#     for i in range(start, n):
#         arr[cur] = li[i]
#         recur(cur + 1, i + 1, a)
#
#
# n, s = map(int, input().split())
# li = list(map(int, input().split()))
# cnt = 0
# # 각 개수의 부분수열에 대해 전부 재귀를 돌려본다.
# for i in range(1, n + 1):
#     arr = [0] * n
#     recur(0, 0, i)
# print(cnt)

def recur(cur, total):
    global cnt

    # 종료 조건
    if cur == n:
        return

    # total에 li[cur]를 먼저 넣고 시작하는 이유는,
    # 종료조건이 위에 있기 때문에, 공집합을 처리하지 않기 위해서.
    total += li[cur]

    # 합이 s과 일치하면 cnt +1
    if total == s:
        cnt += 1

    # 분기처리 // li[cur]를 넣을지, 안넣을지
    recur(cur + 1, total - li[cur])
    recur(cur + 1, total)


n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
recur(0, 0)
print(cnt)