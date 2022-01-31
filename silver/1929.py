# 1929. 소수 구하기
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
 
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 처음 - 틀린 풀이
# import sys
# n, m = map(int, sys.stdin.readline().split(" "))

# li = []
# for i in range(n, m+1):
#     li.append(i)

# for i in li:
#     if i == 1:
#         pass
#     elif i != 2 and i % 2 == 0:
#         pass
#     elif i != 3 and i % 3 == 0:
#         pass
#     elif i != 5 and i % 5 == 0:
#         pass
#     elif i != 7 and i % 7 == 0:
#         pass
#     else:
#         print(i)



n, m = map(int, input().split(" ")) # 입력 받기
sieve = [True] * (m+1) #1 부터 m+1까지의 True로 이루어진 리스트
# m+1을 사용하는 이유는 문제에서 m 이하라고 했기 때문.

o = int((m+1) ** 0.5) #(m+1) ** 0.5까지의 수만 확인하면 됨.
for i in range(2, o + 1): # 2부터 확인 시작
    if sieve[i] == True:
        for j in range(i+i, m+1, i): #예를 들어 3일때, 6부터 3의 배수를 제거
            sieve[j] = False

for i in range(n, m+1): #Ture값의 인덱스로 출력함.
    if sieve[i] == True and i != 1:
        print(i)
