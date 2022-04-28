# 3584. 가장 가까운 공통 조상

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    # 부모 자식관계가 모두 주어지므로 1차원 배열로 진행한다.
    par = [0] * (n + 1)

    for i in range(n - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        # 부모자식관계
        par[b] = a

    x, y = map(int, sys.stdin.readline().strip().split())

    # 두 숫자가 처음부터 같은 조상을 가졌을 수도 있으므로, 나올 수 없는
    # 조상노드를 미리 입력해놓았다.
    par_a = [-1]
    while x:
        par_a.append(x)
        x = par[x]

    par_b = [-2]
    while y:
        par_b.append(y)
        y = par[y]
    
    # 뒤에서부터 달라지는 지점 찾기
    for i in range(-1, -10000, -1):
        if par_a[i] != par_b[i]:
            break

    print(par_a[i + 1])
