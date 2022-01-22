# 2108번: 통계학
# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.


# 입력 :
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력 :
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
n = int(sys.stdin.readline())

li = [] # len(li)
for i in range(n):
    li.append(int(sys.stdin.readline()))


def a_1(a): #산술평균
    return round(sum(a)/len(a))

def a_2(a): #중앙 값
    a.sort()
    return a[(len(a)//2)]

def a_3(a): #최빈값 / 딕셔너리 이용
    check_n = {}
    for i in a:
        if i in check_n: # 딕셔너리에 원래 있던 경우 +1
            check_n[i] += 1
        else: # 딕셔너리에 없는경우 새로 추가
            check_n[i] = 1

    check_n = sorted(check_n.items(), key = lambda x: x[1], reverse = True) # 있는 개수를 기준으로 정렬
    if n != 1:
        if check_n[0][1] == check_n[1][1]:
            return check_n[1][0]
        else:
            return check_n[0][0]
    else:
        return check_n[0][0]

def a_4(a):
    return max(a)-min(a) # 범위 

answer = [a_1(li), a_2(li), a_3(li), a_4(li)]

for i in answer:
    print(i)