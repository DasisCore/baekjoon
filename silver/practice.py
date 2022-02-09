# 이곳은 문제를 풀며 자유롭게 코드를 짜볼 수 있는 공간입니다.


li = list(map(int, input()))
li.sort()

answer = []
for i in range(0, len(li)):
    if len(answer) > 2 and li[i] == answer[-1] and li[i] == answer[-2]:
        answer.pop()
        answer.pop()
    else:
        answer.append(li[i])

if len(answer) > 3:
    if answer[3] + 1 == answer[4] and answer[4] + 1 == answer[5]:
        print("babygin!")
    else:
        print("No babygin!")
elif answer[0] == answer[1] == answer[2]:
    print("babygin!")
elif answer[0] + 1 == answer[1] and answer[1] + 1 == answer[2]:
    print("babygin!")
else:
    print("No babygin")