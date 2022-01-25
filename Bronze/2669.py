# 2669번: 직사각형 네개의 합집합의 면적 구하기
# 문제
# 평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
# 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

# 입력 :
# 입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

# 출력 :
# 첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.


#이 문제는 완전탐색 문제라고 한다.
space = {}
for i in range(1, 101):
    for j in range(1, 101): #100, 100 좌표에 대한 딕셔너리 각 키의 초기 벨류값 0
        space[i, j] = 0 #100,100 좌표에 대한 모든 딕셔너리 값 만들기

for i in range(4):
    x, y, z, r = input().split(" ")
    for i in range(int(x), int(z)): 
        for j in range(int(y), int(r)):
            space[i, j] = 1#사각형에 해당하는 모든 구역은 벨류값을 1로 설정

print(sum(space.values())) #모든 벨류값의 합. = 사각형의 넓이