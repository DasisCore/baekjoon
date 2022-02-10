# 이곳은 문제를 풀며 자유롭게 코드를 짜볼 수 있는 공간입니다.

# 두 수의 최대공약수 구하기
def prime(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

a, b = map(int, input().split())
N = b // a

li = [] # N의 약수 구하기
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        li.append(i)
        if i * i != N:
            li.append(N // i)
li.sort()

srs = 999999999999

# 투포인터 사용
s = 0
e = len(li) - 1

while s < e:
    if li[s] * li[e] == N and prime(li[s], li[e]) == 1:
        if li[s] + li[e] < srs:
            srs = li[s] + li[e]
            x = li[s]
            y = li[e]
        s += 1
        continue
    elif li[s] * li[e] > N:
        e -= 1
    else:
        s += 1

if a == b:
    print(a, a)
else:
    print(a * x, a * y)