# 1991 트리 순회
# https://www.acmicpc.net/problem/1991

import sys

input = sys.stdin.readline
N = int(input().strip())
tree = {} # 딕셔너리로 트리 구현

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식
def preorder(root): # 전위 순회
    if root != '.': # 루트 노드가 .이 아니면 (자식이 있다면)
        print(root, end='')  # root 루트 출력
        preorder(tree[root][0])  # left 재귀적으로 왼쪽 노드 탐색
        preorder(tree[root][1])  # right  재귀적으로 오른쪽 노드 탐색


# 중위 순회 : 왼쪽 자식 -> 루트 ->  오른쪽 자식
def inorder(root):
    if root != '.': # 루트 노드가 . 이 아니면
        inorder(tree[root][0])  # left 재귀적으로 왼쪽 노드 탐색
        print(root, end='')  # root 루트 출력
        inorder(tree[root][1])  # right 재귀적으로 오른쪽 노드 탐색


# 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left 재귀적으로 왼쪽 노드 탐색
        postorder(tree[root][1])  # right 재귀적으로 오른쪽 노드 탐색
        print(root, end='')  # root 루트 출력


# 루트 노드 'A'
preorder('A')
print()
inorder('A')
print()
postorder('A')