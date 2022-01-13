# 10871. X보다 작은 수
# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# 출력 :
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

in_ = input()
in_ = in_.split(" ")
in_ = list(map(int, in_)) #받은 입력값을 리스트화 시킴.

nums = input()
nums = nums.split(" ")
nums = list(map(int, nums)) #두번째로 입력받은 값도 리스트화 해 정리.

count = 0
output = []
for i in range(0, in_[0]): #in_[1] = 5
    if nums[i] < in_[1]:
        count += 1
        output.append(nums[i])

blank = ""
for i in output:
    blank = blank+ str(i) + " "
print(blank)


