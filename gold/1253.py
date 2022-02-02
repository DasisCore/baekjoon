# 1253. 좋다
# 문제
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

# 입력
# 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

# 출력
# 좋은 수의 개수를 첫 번째 줄에 출력한다.

# n = int(input())
# li = list(map(int, input().split()))
# li.sort()

# s = 0
# e = n - 1

# x = li[0]
# y = li[n - 1]

# cnt = 0
# while s < e:
#     if x + y in li:
#         x = li[s]
#         y = li[e]
#         cnt += 1

#     e -= 1
#     y = li[e]
#     if s == e:
#         s += 1
#         x = li[s]
#         e = n - 1
#         y = li[n - 1]

# print(cnt) 
# 풀이는 x, y가 다르면 좋은 수가 같아도 카운트가 +1이라서 틀림.

n = int(input())
li = list(map(int, input().split()))
li.sort()

s = 0
e = n - 1

x = li[0]
y = li[n - 1]

cnt = 0
for i in range(n):
    temp = li[:i] + li[i+1:] #i를 제외한 임시 리스트
    while s < e:
        total = temp[s] + temp[e]
        if total == li[i]:
            cnt += 1
            break        
        elif total < li[i]:
            s += 1
        else:
            e -= 1

print(cnt)