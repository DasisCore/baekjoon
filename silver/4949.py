# 4949. 균형잡힌 세상
# import sys

# b = 1
# string = []
# while b:
#     a = sys.stdin.readline().strip()
#     if a == '.':
#         b = False
#     else:
#         string.append(a) #각 입력에 대한 리스트

# for i in string:
#     redu = [] #[]()를 간추려서 담을 리스트
#     for i in string:
#         for j in i:
#             if j == '[' or j == ']' or j == '(' or j == ')':
#                 redu.append(j)

#     while redu.count('(') != 0 or redu.count('[') != 0:
#         try:    
#             if '(' in redu:
#                 redu.remove('(')
#                 redu.remove(')')
#             elif '[' in redu:
#                 redu.remove('[')
#                 redu.remove(']')
#         except ValueError:
#             print('no')
#             break
#     else:
#         print("yes")



def bracket(string):
    for i in string:
        if i == '(' or i == '[':
            li.append(i)

        if i == ')': 
            if li and li[-1] == '(': # li가 비어있지 않고, li[-1]이면 =  짝이 맞으면
                li.pop() # 짝이 맞으면, '('를 없앰.
            elif not li or li[-1] != '(': #li가 비어있거나, li[-1]이 '('이 아니면
                return 1
        
        if i == ']':
            if li and li[-1] == '[':
                li.pop()
            elif not li or li[-1] != '[':
                return 1
    return 0 #문자열을 다 돌았는데 걸리는 것이 없는 경우.

while True:
    string = input()
    li = []
    if string == '.':
        break
    true = bracket(string)
    if true == 0 and not li:
        print('yes')
    else:
        print('no')