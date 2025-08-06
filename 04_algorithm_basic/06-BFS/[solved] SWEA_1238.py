import sys
sys.stdin = open('./SWEA_input_datas/input_1238.txt')

from collections import deque

def bfs(node, step): # node, step: 현재까지 몇번 이동했는지 저장
    queue = deque([(node, step)])
    visited[node] = True # 방문 체크

    # 최대 step, 최대 node의 수 초기화
    max_step = 0
    max_nodes = []

    # print(f"초기 queue: {list(queue)}")  # 초기 상태 출력

    while queue: # queue에 요소가 있는 동안
        current, step = queue.popleft() # current: 현재 node, step: 현재까지 이동한 횟수
        # print(f"popleft -> current: {current}, step: {step}, queue: {list(queue)}")

        if step > max_step: # 현재까지 최대 max_step보다 현재의 step이 더 크면 ( 더 많이 움직였으면)
            max_step = step
            max_nodes = [current] # 새로운 최대 step이 등장하면 리스트 초기화
        elif step == max_step:
            max_nodes.append(current)

        # 현재 노드 처리 로직
        for neighbor in graph.get(current, []):
            if not visited[neighbor]:
                queue.append((neighbor, step+1))
                # print(f"append -> neighbor: {neighbor}, step: {step+1}, queue: {list(queue)}")
                visited[neighbor] = True

    return max(max_nodes)

T = 10
for t in range(1, T+1):
    N, start = map(int, input().strip().split()) # N: 데이터의 길이, start: 시작점
    datas = list(map(int, input().strip().split()))
    max_node = max(datas) # 최대 노드의 숫자
    visited = [False] * (max_node+1) # 최대 노드 수보다 많은 visited 생성

    # 간선 정보 받아온 뒤 graph에 저장
    graph = {}
    # 0번 idx는 from, 1번 idx는 to, 2번 idx는 from, 3번 idx는 to ...
    for i in range(0, len(datas), 2):  # 2씩 증가하면서 from, to 저장
        if datas[i] not in graph.keys(): # from (dict의 key)가 존재하지 않으면
            graph[datas[i]] = [] # 빈 리스트 추가

        graph[datas[i]].append(datas[i+1]) # from의 value list에 추가


    max_node = bfs(start, 0)
    print(f"#{t} {max_node}")







