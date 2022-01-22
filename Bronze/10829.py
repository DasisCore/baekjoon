# 10829. 이진수
# 문제
# 자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

# 출력 :
# N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

def recur(a):
    if a < 1: # 0보다 작은경우 0으로 리턴
        return a
    elif a == 1: # 1인경우 
        return '1'
    elif a % 2: #홀수인 경우
        return recur(a//2) + "1"
    else: #짝수인 경우
        return recur(a//2) + '0'

n = int(input())
print(recur(n))