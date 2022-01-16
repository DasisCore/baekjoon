# 1181. 단어 정렬

# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

test = int(input()) #단어의 개수 N

dic = [] #단어를 입력받아 리스트에 저장
for i in range(test):
    dic.append(input())

so = []
last = []
for i in range(test): #단어의 개수와 단어로 이루어진 리스트를 생성
    so.append(len(dic[i]))
    last.append([so[i],dic[i]])
last.sort() #단어의 개수를 기준으로 정렬 , 이제 중복만 제거하면 됨.

answer = []
for i in range(len(last)):
    if last[i][1] not in answer: # answer안에 같은 값이 없을 경우만 리스트에 추가
        answer.append(last[i][1])

for i in range(len(answer)):
    print(answer[i])