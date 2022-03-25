# 15565. 귀여운 라이언

# 문제
# 꿀귀 라이언 인형과, 마찬가지로 꿀귀인 어피치 인형이 N개 일렬로 놓여 있다. 라이언 인형은 1, 어피치 인형은 2로 표현하자. 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구하여라.
#
# 입력
# 첫 줄에 N과 K가 주어진다. (1 <= k <= n <= 10^6)
# 둘째 줄에 N개의 인형의 정보가 주어진다. (1 또는 2)
#
# 출력
# K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기를 출력한다. 그런 집합이 없다면 -1을 출력한다.

################################################################################################

n, k = map(int, input().split())
li = list(map(int, input().split()))
s = 0
e = 0

answer = n + 1
# 라이언 인형의 개수
cnt = 0
# 집합의 크기
size = 0

while True:

    # e가 n에 도착했을 때, 더 작은 size를 찾기 위해 s를 밀어준다.
    if e == n:
        # 더 찾을 필요가 없으면
        if cnt < k:
            break

        # size의 최솟값 갱신
        answer = min(answer, size)

        # s를 밀며 최소 크기를 찾는다.
        if li[s] == 1:
            cnt -= 1
            size -= 1
            s += 1
        else:
            size -= 1
            s += 1
    
    # 라이언 인형의 개수가 작을 경우 e를 밀며 라이언 인형을 찾는다
    elif cnt < k:
        if li[e] == 1:
            cnt += 1
            size += 1
            e += 1
        else:
            size += 1
            e += 1

    # 라이언 인형을 k개 찾았을 경우, 더 작은 사이즈를 찾기 위해
    # s를 뒤로 밀어준다.
    # 하지만 e가 n에 도달 했을 경우에는
    # 의미없이 e가 계속 커지는 일이 있어 e == n일 때는 따로 처리해줬다.
    elif cnt == k:
        answer = min(answer, size)
        if li[s] == 1:
            cnt -= 1
            size -= 1
            s += 1
        else:
            size -= 1
            s += 1

# 정답이 갱신되지 않았을 경우 -1 출력
if answer == n + 1:
    print(-1)
else:
    print(answer)


#################################################################

n, k = map(int, input().split())
li = list(map(int, input().split()))
s = 0
e = 0

answer = n + 1
# 라이언 인형의 개수
cnt = 0
# 집합의 크기

while True:
    # 라이언 인형을 k개 찾았을 때,
    if cnt == k:
        # 인형의 개수는 size가 아닌 e - s로 처리한다.
        answer = min(answer, e - s)

        # li[s]가 1일 경우 갯수를 빼고 s를 밀어준다.
        if li[s] == 1:
            cnt -= 1
        s += 1

    # 평소에 s를 꾸준히 밀어주므로, e == n 일때 반복문을 종료한다.
    elif e == n:
        break

    # 라이언 인형이 k보다 작을 경우
    else:
        # e를 밀어 라이언 인형을 확보한다.
        if li[e] == 1:
            cnt += 1
        e += 1

# answer가 n + 1보다 작을 경우 answer 출력.
# 아닐 경우 -1 출력 (pytonic!!!)
print(answer if answer < n + 1 else -1)
