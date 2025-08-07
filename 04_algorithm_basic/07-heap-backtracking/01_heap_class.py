class MinHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화 (완전 이진트리로 구현할 것이니까)
        self.length = 0  # 힙의 길이 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self.length += 1  # 힙의 길이 증가
        self._siftup(self.length-1)

    # 힙에서 최소 요소를 제거하고 반환
    def heappop(self):
        if self.length == 0:
            raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
        root = self.heap[0]
        # 마지막 요소를 루트로이동
        self.heap[0] = self.heap.pop()
        # 내 길이를 1 감소
        self.length -= 1
        # 힙의
        return root
        
    # 주어진 리스트을 힙으로 변환
    def heapify(self, array):
        self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
        self.length = len(array)        

    # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftup(self, idx):
        # 마지막에 삽입된 노드와 부모 노드의 크기를 비교
        # 부모 노드의 인덱스를 얻어야 한다
        parent = (idx-1) // 2
        # 최소힙을 구현하고 있는 중
        # 언제까지 시트프업이 이루어져야 하는가?
        '''
            최소힙을 구현하고 있는 중!
            언제까지 시프트업이 이루어 져야 하는가?
            1. 내 idx가 0이 되기 전까지
            2. 내 값이 부모 노드의 값보다 작은 동안
        '''
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent # 내 위치를 부모와 스왑했으니 갱신
            parent = (idx-1) // 2 # 부모 정보 갱신

    # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftdown(self, idx):
        '''
        1. 가장 작은 요소를무엇으로 볼 것인지 담을 수 있는 변수 초기화
            - 첫 시작 과정에서는 일단 루트를 smallest로 지정
        2. 왼쪽 자식의 인덱스를 계산
        3. 오른쪽 자식의 인덱스를계산
        '''
        smallest = idx
        left = 2 * idx + 1 # root가 0이니까 +1 해야 1번 노드가 됨
        right = 2 * idx + 2

        # 왼쪽 자식의 인덱스가 내 전체 크기를 벗어나지 않고
        if left < self.length and self.heap[left] < self.heap[smallest]:
            smallest = left # 우선 인덱스만 바꾼 것
        if right < self.length and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx: # 내가 제일 작은게 아니면
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.hea[smallest]

    def __str__(self):
        return str(self.heap)  # 힙의 문자열 표현 반환

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]

min_heap.heapify([5, 4, 3, 2, 1])
print(min_heap)  # [1, 2, 3, 5, 4]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 4, 3, 5] 
print(min_heap.heappop())  # 2
print(min_heap)  # [3, 4, 5]