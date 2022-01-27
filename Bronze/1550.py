# 1550. 16진수
# 문제
# 16진수 수를 입력받아서 10진수로 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 16진수 수가 주어진다. 이 수의 최대 길이는 6글자이다. 16진수 수는 0~9와 A~F로 이루어져 있고, A~F는 10~15를 뜻한다. 또, 이 수는 음이 아닌 정수이다.

# 출력
# 첫째 줄에 입력으로 주어진 16진수 수를 10진수로 변환해 출력한다.

n = input()
# print(int(n, 16))

word = ""
for i in range(len(n)-1, -1, -1):
    word += n[i] # 다 만들고 나서 reverse를 쓰면 된다는걸 깨달았다.
#word = word.reverse()

total = 0
for i in range(len(word)): #word의 각 자리수에 따라 16**i를 곱한다.
    a = word[i].upper()
    if a == 'A':
        total += 10*(16**i)
    elif a == 'B':
        total += 11*(16**i)
    elif a == 'C':
        total += 12*(16**i)
    elif a == 'D':
        total += 13*(16**i)
    elif a == 'E':
        total += 14*(16**i)
    elif a == 'F':
        total += 15*(16**i)
    else:
        total += int(a)*(16**i)

print(total)

