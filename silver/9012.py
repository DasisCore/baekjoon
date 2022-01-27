# 9012. 괄호 

# def ps(word):
#     for i in word:
#         if i == '(':
#             li.append(i)

#     for i in word:
#         if i == ')':
#             if li:
#                 li.pop()
#             elif not li:
#                 return 1
#     return 0

# n = int(input())

# for i in range(n):
#     li = []
#     word = input()
#     sol = ps(word)
#     if sol == 0 and not li:
#         print("YES")
#     else:
#         print("NO")

n = int(input())

for i in range(n):
    a = input()
    li = []

    for i in a:
        if i == '(':
            li.append(i) #'('를 만나면 리스트에 추가함
        elif i == ')': #')'를 만났을 경우
            if li and li[-1] == '(': #리스트가 비어있지 않고, li[-1]이 '('면
                li.pop() #리스트에서 '('을 제거함
            else: #리스트가 비어있거나, li[-1]이 ')'일 경우
                li.append(i) #리스트에 ')' 추가
                break

    if li: #리스트에 무언가 있으면 NO 없으면 YES
        print('NO')
    else:
        print('YES')