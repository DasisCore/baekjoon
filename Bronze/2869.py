# 2869. 달팽이는 올라가고 싶다.
# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력 :
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

num = input()
num =num.split(" ")
num = list(map(int, num))

# A : 오름(num[0]), B : 미끌(num[1]), V : 막대 높이(num[2])

# try1 = num[2] // num[0]
# hike = 0
# if num[0]*1 > num[2]:
#     print(1)

# if num[2] / num[0] > 1:
#     for i in range(2, num[2]):
#         hike = num[0]*i
#         answer = hike - num[1]*i
#         answer = answer + num[0]
#         if answer > num[2]:
#             print(i)
#             break

one_day = num[0] - num[1]
day = (num[2] - num[0])//num[0]

for i in range(1, day + 3):
    if num[0] > num[2]:
        print(1)
    elif one_day*i > num[2] - num[0]:
        print(i+1)