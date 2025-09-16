'''
후위 표기식 바꾸는 프로그램
queue = []
if 숫자이면 queue에 삽입
elif 연산자이면 pop -> push
    이때, 빈 queue이면 그냥 push만
'''
import sys
sys.stdin = open('./SWEA_input_datas/input_1222.txt')

from collections import deque

T = 1
for t in range(1, T+1):
    N = int(input())
    inputs = input().strip()
    queue = deque()
    result = 0

    for elem in inputs:
        if elem.isnumeric():
            queue.append(int(elem))
        elif elem == '+':
            if not queue:
                print('잘못된 수식입니다.')
            else:
                popped = queue.popleft()

                queue.append(popped)

    print(f"#{t} {result}")

