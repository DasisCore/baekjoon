# 1991. 트리 순회

# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
# 예를 들어 위와 같은 이진 트리가 입력되면,
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)가 된다.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

#########################################################################################################

def pre_order(v):
    if v:
        print(chr(v + 64), end="")
        pre_order(ch1[v])
        pre_order(ch2[v])

def in_order(v):
    if v:
        in_order(ch1[v])
        print(chr(v + 64), end="")
        in_order(ch2[v])

def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(chr(v + 64), end="")

n = int(input())
ch1 = [0] * 28
ch2 = [0] * 28
for i in range(n):
    a, b, c = map(str, input().split())
    a, b, c = (ord(a) - 64), (ord(b) - 64), (ord(c) - 64)
    if b == -18:
        b = 0
    if c == -18:
        c = 0
    ch1[a] = b
    ch2[a] = c

pre_order(1)
print()
in_order(1)
print()
post_order(1)
