# 2164번: 카드2
# 문제
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

# 출력 :
# 첫째 줄에 남게 되는 카드의 번호를 출력한다.

# import sys #재귀함수 풀이

# #위의 과정을 반복하는 재귀함수.
# def recur(a):
#     if len(a) == 1: #정지조건
#         return a
#     else:
#         b = a[1:] #한장 버리기.
#         c = b[1:] #맨 앞 한장을 뒤로 보내기.
#         c.append(b[0])
#         return recur(c)

# n = int(sys.stdin.readline())

# card = []
# for i in range(1, n+1): #카드 덱 만들기
#     card.append(i)

# print(*recur(card))

#---------------------------------------------

# import sys #반복문 풀이

# n = int(sys.stdin.readline())

# card = []
# for i in range(1, n+1): #카드 덱 만들기
#     card.append(i)

# b = card
# c= []
# for i in range(n-1):
#     b = b[1:] #한장 버리기
#     c = b[1:] #맨 앞 한장을 뒤로 보내기.
#     c.append(b[0]) #맨 뒤에 한장 추가
#     b = c #카드 상태 초기화

# print(*c)

#-------------------------- 모듈을 이용한 풀이

from collections import deque
import sys

n = int(sys.stdin.readline())
card_list = [i for i in range(1, n+1)]

deq = deque(card_list)
while len(deq) > 1:
    deq.popleft() #맨 왼쪽 값 뽑아내기
    deq.append(deq.popleft()) #카드 옮기기
print(deq.pop())
