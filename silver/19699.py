# 19699. 소-난다!

# 문제
# 지난 번 헛간 청약의 당첨우(牛)가 발표됐다. 청약에 당첨된 소들은 날아갈 듯이 기뻐하다가 진짜로 하늘을 날았다. 하지만 이후로 소들은 날 수 없었다. 그러던 어느 날, 꿀벌에게 쏘이면 잠깐 하늘을 날 수 있다는 사실을 깨달았다. 이 사실이 퍼지자 소들은 다시 자유롭게 하늘을 날기 시작했다.
# 소들이 하늘을 날며 우(牛)통사고가 빈번해지자, 농부 존은 소들이 하늘을 나는 것에 제한을 두었다. 소들은 항의했지만 소들의 항의는 받아들여지지 않았다.
# 농장에는 N마리의 소가 있다. 농부 존은 소들의 몸무게의 합이 소수(prime)가 되도록 M마리의 소를 선별할 계획이다. 농부 존의 계획에 맞게 소를 선별했을 때 나올 수 있는 몸무게의 합을 모두 출력하시오.
#
# 입력
# 첫째 줄에 농장에 있는 소들의 수 N, 선별할 소의 수 M이 주어진다.
# 둘째 줄에 소들의 몸무게 H_i가 주어진다.
#
# 출력 :
# M마리 소들의 몸무게 합으로 만들 수 있는 모든 소수를 오름차순으로 출력한다. 만약 그러한 경우가 없다면 -1을 출력한다.
#
# ##########################################################################################

# 합이 소수인지 확인하는 함수
def check(lst):
    global answer

    num = sum(lst)
    cnt = 0
    for i in range(1, num + 1):
        # 불필요한 계산을 막기 위해
        if i * i > num:
            break
        if num % i == 0:
            cnt += 1

    # 소수이면 리스트에 넣는다
    if cnt == 1 and num not in answer:
        answer.append(num)
    return


# 백 트래킹을 이용해 조합을 만들어내는 함수
def recur(cur):
    if cur == m:
        check(arr)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        arr[cur] = li[i]
        recur(cur + 1)
        visited[i] = 0


n, m = map(int, input().split())
li = list(map(int, input().split()))
arr = [0] * m
visited = [0] * n

# 답을 담을 변수 answer
answer = []
recur(0)
if not len(answer):
    print("-1")
else:
    answer.sort()
    print(*answer)

