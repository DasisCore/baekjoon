# 10816. 숫자 카드 2
# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

import sys #숫자를 조금이라도 빨리 받기 위한 발악

num_1 = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().strip().split(" ")))
num_2 = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
# 입력값 받기.

answer = {} #딕셔너리를 이용한 풀이.
for i in nums: #카드 숫자를 담을 키값을 미리 만들어둠
    answer[i] = 0

for i in card: # 키값과 일치하는 카드가 있으면 갯수를 +1 한다.
    if i in answer:
        answer[i] += 1

last = [] 
for i in nums:
    last.append(answer[i])
print(*last)
#이 문제에서 놓치기 쉬운 곳인데, 네번째 주어지는 숫자가 중복된 것이 있으면
# 하나만 나오지 않고, 여러 개가 나오도록 여기서 다듬어 주어야 한다.


# + 22-03-24 2번째 풀이

n = int(input())
li = sorted(list(map(int, input().split())))
m = int(input())
arr = list(map(int, input().split()))

for i in arr:
    s = 0
    e = n - 1

    answer1, answer2 = 1, 0

    while s <= e:
        mid = (s + e) // 2

        if li[mid] == i:
            answer1 = mid
            e = mid - 1

        elif li[mid] < i:
            s = mid + 1

        else:
            e = mid - 1

    s = 0
    e = n -1
    while s <= e:
        mid = (s + e) // 2

        if li[mid] == i:
            answer2 = mid
            s = mid + 1

        elif li[mid] < i:
            s = mid + 1

        else:
            e = mid - 1

    print(answer2 - answer1 + 1)