# 24060. 알고리즘 수업 - 병합 정렬 1

# 문제
# 오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.
# 크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.
#
# merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합
#     }
# }
#
# # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# # A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
# merge(A[], p, q, r) {
#     i <- p; j <- q + 1; t <- 1;
#     while (i ≤ q and j ≤ r) {
#         if (A[i] ≤ A[j])
#         then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
#         else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
#     }
#     while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[i++];
#     while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[j++];
#     i <- p; t <- 1;
#     while (i ≤ r)  # 결과를 A[p..r]에 저장
#         A[i++] <- tmp[t++];
# }
#
# 입력
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 108)가 주어진다.
# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)
#
# 출력
# 배열 A에 K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력한다.

##############################################################################################################################


from collections import deque
import math

# 하나씩 정렬 할때마다 카운트를 올려준다.
def check():
    global cnt , ans, a
    cnt += 1
    # 카운트가 k에 도달하였을 때 정답을 갱신해준다.
    if cnt == k:
        ans = a

def merge(left, right):
    global cnt, a
    
    # 정렬하여 넣어 줄 결과 리스트
    result = deque()

    # left와 right가 모두 빌때까지 반복한다.
    while len(left) or len(right):
        # 크기를 비교하여 result에 넣어주는 과정.
        # 수를 넣어줄 때마다 check를 해준다.
        if len(left) and len(right):
            if left[0] <= right[0]:
                a = left[0]
                check()
                result.append(left.popleft())
            else:
                a = right[0]
                check()
                result.append(right.popleft())
        elif len(left) and not len(right):
            a = left[0]
            check()
            result.append(left.popleft())
        elif len(right) and not len(left):
            a = right[0]
            check()
            result.append(right.popleft())
    return result


# 병합 정렬을 위해 반으로 나누고, 이후 병합을 해준다.
def merge_sort(li):

    if len(li) == 1:
        return li

    mid = math.ceil(len(li)/2)
    left = deque()
    right = deque()

    for i in range(mid):
        left.append(li[i])
    for i in range(mid, len(li)):
        right.append(li[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
ans = -1
merge_sort(li)
print(ans)

########################################################################################################

import math

def check():
    global cnt, ans
    cnt += 1

    if cnt == k:
        ans = a

def merge_sort(li):

    if len(li) == 1:
        return li

    mid = math.ceil(len(li)/2)

    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    return merge(left, right)

def merge(left, right):
    global a

    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            a = left[left_idx]
            check()
            result.append(left[left_idx])
            left_idx += 1
        else:
            a = right[right_idx]
            check()
            result.append(right[right_idx])
            right_idx += 1

    if left_idx == len(left):
        while right_idx < len(right):
            a = right[right_idx]
            check()
            result.append(right[right_idx])
            right_idx += 1

    if right_idx == len(right):
        while left_idx < len(left):
            a = left[left_idx]
            check()
            result.append(left[left_idx])
            left_idx += 1

    return result

n, k = map(int, input().split())
li = list(map(int, input().split()))
ans = -1
cnt = 0
merge_sort(li)
print(ans)





