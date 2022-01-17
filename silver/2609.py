# 2609. 최대공약수와 최소공배수

a, b = map(int, input().split(' '))

GCD = []
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        GCD.append(i)
c = int(max(GCD))
print(c)

LCM = b*int(a/c)
print(LCM)