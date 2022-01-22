# 10989. 수 정렬하기 3
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력 :
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# import sys

# n = int(sys.stdin.readline())
# li = []
# for i in range(n):
#     a = int(sys.stdin.readline())
#     li.append(a)
# li.sort()
# for i in li:
#     print(i)
import sys 

n = int(sys.stdin.readline()) 
#input()은 입력에 시간이 많이 걸리기 때문에
# 주로 sys.stdin.readline()을 많이 쓴다고 한다.
li = [0] * 10001 #index 0부터 10001번째까지 있는 리스트 생성
for i in range(n):
    num = int(sys.stdin.readline())
    li[num] = li[num]+1 #해당 인덱스에 있는 숫자에 1씩 더해 개수를 센다.

for i in range(1, 10001):
    if li[i] > 0:
        for j in range(li[i]): #for문을 이용 해당 index의 개수만큼 해당 숫자 출력
            print(i)
