# 2798. 블랙잭
# 문제)
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서,
# 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다.
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에,
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때,
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력)
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력)
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

def check_plus(a):
    if a <= in_put[1]:
        answer.append(a)

in_put = input()
in_put = in_put.split(" ")
in_put = list(map(int, in_put)) #처음 입력값을 받아 N과 M을 분리
# N = in_put[0]  , M = in_put[1]

card = input()
card = card.split(" ")
card = list(map(int, card)) #각 카드의 값을 리스트화


answer = [] # M을 넘지 않는 각 카드의 합
for i in card:
    compare = card[:] #lits card의 값이 사라지면 곤란하므로
    m_answer = 0
    m_answer += i
    f_num = m_answer
    compare.remove(i) #첫번째 카드를 더하고, 리스트에서 제거
    for j in compare:
        m_num = f_num # 첫 카드를 뽑은 값으로 돌아오기 위함.
        m_num += j
        compare.remove(j)
        for k in compare:
            l_num = m_num #두번째 카드까지의 합으로 돌아오기 위함.
            l_num += k
            check_plus(l_num)

print(max(answer))
            