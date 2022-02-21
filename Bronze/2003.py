# 2003. 수들의 합 2

n, m = map(int, input().split())
li = list(map(int, input().split()))

# 투 포인터
s = 0
e = 0

cnt = 0
while e != n:
    a = sum(li[s:e + 1]) # 해당 구간의 합
    if a == m:
        cnt += 1

    if a < m:
        e += 1 # 합이 작으면 e 밀기
    else:
        s += 1 # 합이 크면 e 밀기
print(cnt)