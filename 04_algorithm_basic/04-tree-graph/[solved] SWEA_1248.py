import sys
sys.stdin = open('./SWEA_input_datas/input_1248.txt')

# 각 노드의 조상 찾기: 
def find_all_ancestor(node, ancestor_list):
    # 루트 노드인 1까지 다 돌면 return
    if node == 1:
        return [] # 빈 리스트 반환
    
    # 현재 노드의 조상들을 찾기 위해 재귀 호출
    ancestors = find_all_ancestor(parents[node], ancestor_list)

    # 현재 노드를 조상 리스트에 추가하고 반환
    ancestors.append(node)

    return ancestors


T = int(input())
for t in range(1, T+1):
    # 정점개수, 간선개수, 타겟정점1, 타겟정점2
    V, E, n1, n2 = map(int, input().strip().split())
    infos = list(map(int, input().strip().split()))
    parents = [0] * (V+1) # 부모 노드만 저장된 리스트
    children = [[] for _ in range(V+1)] # 1-based이므로 V+1개 생성 / 자식노드만 저장된 리스트

    # 부모와 자식 node 정보 저장
    for i in range(0, len(infos), 2): # 2씩 증가시키면서
        parents[infos[i]] = infos[i] # 부모 노드의 숫자를 부모노드인덱스에 저장
        children[infos[i]].append(infos[i+1]) # 자식노드를 부모노드인덱스에 리스트로 저장

    
    # 1. 각 정점의 조상 찾기
    n1_parents = n2_parents = []
    
    for i in range(1, len(children)): # 1-based이므로 0은 어차피 정보가 없으므로 1부터 시작
        if n1 in children[i]: # n1노드가 children에 있으면 해당 인덱스의 자식노드라는 의미이므로
            n1_parents.append(i) # n1_parents에 인덱스를 저장
            # 이번에는 children[5]
        if n2 in children[i] : n2_parents.append(i)

    if t == 1:
        print(n1_parents, n2_parents)

    # 2. 공통 조상 찾기 (가장 먼저 등장하는 동일한 부모 노드가 가장 가까운 부모 노드가 됨)

    # 3. 가장 가까운 공통 조상으로부터 서브트리의 개수 세기 (본인 포함)

