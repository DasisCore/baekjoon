# 1411. 비슷한 단어

# 문제
# 만약 어떤 단어A를 숌스럽게 바꿔서 또다른 단어 B로 만든다면, 그 단어는 비슷한 단어라고 한다.
# 어떤 단어를 숌스럽게 바꾼다는 말은 단어 A에 등장하는 모든 알파벳을 다른 알파벳으로 바꾼다는 소리다. 그리고, 단어에 등장하는 알파벳의 순서는 바뀌지 않는다. 두 개의 다른 알파벳을 하나의 알파벳으로 바꿀 수 없지만, 자기 자신으로 바꾸는 것은 가능하다.
# 예를 들어, 단어 abca와 zbxz는 비슷하다. 그 이유는 a를 z로 바꾸고, b는 그대로 b, c를 x로 바꾸면, abca가 zbxz가된다.
# 단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 한 줄에 하나씩 단어가 주어진다. 단어의 길이는 최대 50이고, N은 100보다 작거나 같은 자연수이다. 모든 단어의 길이는 같고, 중복되지 않는다. 또, 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 첫째 줄에 총 몇 개의 쌍이 비슷한지 출력한다.

##############################################################################

import sys

n = int(sys.stdin.readline().strip())
li = [sys.stdin.readline().strip() for i in range(n)]
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        word1 = li[i]
        word2 = li[j]

        flag = True
        check1 = [0] * 26
        check2 = [0] * 26
        for k in range(len(word1)):
            idx1 = ord(word1[k]) - ord('a')
            idx2 = ord(word2[k]) - ord('a')

            if check1[idx1] == 0 and check2[idx2] == 0:
                check1[idx1] = word2[k]
                check2[idx2] = word1[k]
            elif check1[idx1] != word2[k]:
                flag = False
                break
        if flag:
            cnt += 1
print(cnt)
























