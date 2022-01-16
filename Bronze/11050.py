# 11050. 이항 계수 1
# 문제 
# 자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 N과 K가 주어진다.

nums = input()
nums = nums.split(" ")
nums = list(map(int, nums))

n = 1 # N!
for i in range(1, nums[0]+1):
    n *= i

k = 1 # K!
for i in range(1, nums[1]+1):
    k *= i

n_k = 1 #(N-K)!
for i in range(1, nums[0]-nums[1]+1):
    n_k *= i

print(n//(k*n_k))
