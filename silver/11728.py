# 11728. 배열 합치기

# 문제
# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

# 출력 :
# 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

# n, m = map(int, input().split())
# li_1 = list(map(int, input().split())) + [0]
# li_2 = list(map(int, input().split())) + [0]

# s = 0
# e = 0

# while True:
#     if li_1[s] <= li_2[e]:
#         print(li_1[s], end=" ")
#         s += 1
#     if li_1[s] > li_2[e]:
#         print(li_2[e], end=" ")
#         e += 1
#     if li_1[s] == li_1[n]: #li_1이 끝에 도달하면 
#         print(*li_1[s:-1], end= "")
#         if li_2[e] > li_1[s]:
#             print(*li_2[e:-1]) #li_2의 나머지를 출력
#             break
#     if li_2[e] == li_2[m]: #li_2이 끝에 도달하면
#         print(*li_2[e:-1], end= "")
#         if li_2[e] < li_1[s]:
#             print(*li_1[s:-1]) #li_1의 나머지를 출력
#             break


N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

s, e = 0, 0

while s != N or e != M:
    if s == N:
        print(B[e], end=" ")
        e += 1
    elif e == M:
        print(A[s], end=" ")
        s += 1
    else:
        if A[s] < B[e]:
            print(A[s], end= " ")
            s += 1
        else:
            print(B[e], end= " ")
            e += 1