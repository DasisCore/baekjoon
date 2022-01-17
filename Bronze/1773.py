# 1773. 폭죽쇼
문제
학생들은 3주가 지난 기념으로 매점에서 1월 1일이 지나 싸게 파는 폭죽을 사서 터뜨리고 있다.
폭죽쇼를 하는 동안 N명의 학생들이 폭죽을 터뜨린다. 그리고 이 N명의 학생은 각각 일정한 주기로 폭죽을 터뜨린다. 
물론 이 주기는 학생들마다 같을 수도, 다를 수도 있다. 그리고 우리는 초 단위로 관찰을 하고, 폭죽 역시 초 단위로 터진다.
폭죽쇼가 끝날 때까지 얼마나 많은 시간동안 밤하늘에 폭죽이 터지는 것을 볼 수 있는지 궁금해 하는 조교를 도와주자.

입력 :
첫 줄에 폭죽을 터뜨리는 학생의 수 N(1 ≤ N ≤ 100)과 폭죽쇼가 끝나는 시간 C(1 ≤ C ≤ 2,000,000)가 주어진다.
 그 다음 N개의 줄에는 학생들이 폭죽을 터뜨리는 주기가 한 줄에 하나씩 주어진다. 주기는 1보다 크거나 같고, C보다 작거나 같은 자연수이다.

출력 :
폭죽쇼가 시작되고 끝날 때까지 밤하늘에 폭죽을 볼 수 있는 총 시간을 출력한다.

nums = input().split(" ")
nums = list(map(int, nums))

a = [int(input()) for i in range(0, nums[0])]
# a[0], a[1]
b = set()

for i in range(0, nums[0]):
    for j in range(a[i], nums[1]+1, a[i]):
        b.add(j)
print(len(b))

#------------------------------------------------------------

nums = input().split(" ")
nums = list(map(int, nums)) 
# N = num[0], C = num[1]
check = [False]*(nums[1]+1) #전부 false인 리스트
ans = 0
for i in range(nums[0]): #사람 수 만큼 입력
    n = int(input())
    for i in range(n, nums[1]+1, n): #한 학생의 폭죽 주기
        if not check[i]: #check[i]가 False면 코드 실행
            check[i] = True #한 학생의 주기들을 True로 바꿈
            ans += 1 #카운팅
print(ans)

#-------------------------------------------------------------

nums = input().split(" ")
nums = list(map(int, nums)) 
people = [0 for i in range(nums[1]+1)]

for i in range(nums[0]):
    a = int(input())
    for i in  range(a, nums[1]+1, a):
        people[i] = 1

print(sum(people))