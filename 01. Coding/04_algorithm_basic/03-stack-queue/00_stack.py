class Stack:
    # 생성자 함수
    def __init__(self, capacity=10):
        self.capacity = capacity # 이 자료구조의 최대 수용 가능 공간
        self.items = [None] * capacity
        self.top = -1

    # 주어진 값을 삽입
    def push(self, item):
        self.top += 1 # 올바른 삽입 위치 찾기
        # 예외 처리 -> is_full 하다면 ... 어떠한 처릴
        self.items[self.top] = item
    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!')
            return
        item = self.items[self.top]
        self.items[self.top] = None
        self.top += 1
        return item

    def is_full(self):
        # stack이 가득 찼음을 어떻게 알 수 있을까?
        return self.capacity -1 == self.top

    def is_empty(self):





stack = [] # list를 사용해서 자료구조 stack을 구현한다

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack[-1])
print(len(stack))
print(stack.pop())
print(stack.pop())
