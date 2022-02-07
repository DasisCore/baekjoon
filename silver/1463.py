# 1463. 1로 만들기

n = int(input())

dp = [0] * (n+1)
dp[1] = 0
dp[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + 1



# li = [0, 1]
# def fib(n):
#     if n >= 2:
#         for i in range(2, n+1):
#             li.append(li[i-1] + li[i-2])
#     return li[n]

# print(fib(10))