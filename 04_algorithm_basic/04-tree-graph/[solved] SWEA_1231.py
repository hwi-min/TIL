import sys
sys.stdin = open('./SWEA_input_datas/input.txt')


# 중위 순회 함수 정의
def inorder(idx):
    if left[idx]: # 왼쪽 자식이 있으면
        inorder(left[idx])
    print(tree[idx], end='') # 중위 순회 (왼쪽 자식이 없으면 바로 부모노드 출력)

    if right[idx]:
        inorder(right[idx])
    
T = 10
for t in range(1 ,T+1):
    N = int(input()) # 정점의 수
    tree = [[]  for _ in range(N+1)] # 1-based 이므로 N+1개 생성
    left, right = [0] * (N+1), [0] * (N+1) # 자식 정보 저장할 list 생성

    for _ in range(N):
        info = input().strip().split() # split한 리스트 결과를 info에 저장
        idx = int(info[0]) # 노드의 인덱스 idx로 저장
        tree[idx] = info[1] # 노드의 인덱스에 문자 저장
        if len(info) >= 3: # 자식이 하나라도 있으면
            left[idx] = int(info[2]) # 왼쪽 자식 저장
            if len(info) == 4:
                right[idx] = int(info[3]) # 오른쪽 자식 저장
    print(f"#{t}", end=' ')
    inorder(1)
    print()

