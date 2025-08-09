import sys
sys.stdin = open("./SWEA_input_datas/sample_input_5176.txt")

def inorder(node):
    global number

    if node * 2 <= N:
        inorder(node * 2)

    tree[node] = number
    number += 1

    if node * 2 + 1 <= N:
        inorder(node*2+1)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    number = 1
    tree = [0] * (N+1)

    inorder(1)

    print(f"#{t} {tree[1]} {tree[N//2]}")