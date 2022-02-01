# 이곳은 문제를 풀며 자유롭게 코드를 짜볼 수 있는 공간입니다.
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * (n+1)

#     for i in range(2, n + 1):
#         if i * i > n:
#             break
#         if not sieve[i]:
#             continue
#     for j in range(i * i, n + 1, i):
#         sieve[i] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

# print(prime_list(16))

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    i = 2
    while i * i <= n:
        if not sieve[i]:
            continue
        
        for i in range(i * i, n + 1, i):
            sieve[i] = False
        
        i += 1

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(16))
