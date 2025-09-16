def BFS(root_node):
    '''
    :param root_node: 너비 우선 탐색을 시작할 서브 트리의 루트
    :return: 완성된 경로
    '''
    result = [] # 탐색 경로를 저장할 리스트
    # 이번에 조사할 노드와 앞으로 조사할 노드들 (후보군)을 담을 자료구조
    data_structure = [root_node]
    # 탐색이라고 하는 행위를 언제까지 할 것이냐?
    # 모든 노드를 다 탐색해서 더 이상 탐색할 후보군이 없을 때까지!
    while data_structure:
        node = data_structure.pop(0) # FIFO
        result.append(node)
        for child in graph.get(node, []):
            # 다음 조사 후보군 목록에 자식을 추가한다.
            data_structure.append(child)
    return result



# 그래프 인접 리스트
graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I'], 
    'E': [],
    'F': [],
    'G': [],
}

start_node = 'A'
print(BFS(start_node))
