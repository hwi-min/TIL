import sys
sys.stdin = open('./SWEA_input_datas/input_1225.txt')

from collections import deque


T = 10
for t in range(1, T+1):
    _ = int(input())
    nums = list(map(int, input().strip().split()))
    queue = deque(nums)
    step = 1

    while queue:
        current = queue.popleft()
        current -= step

        if current <= 0:
            queue.append(0)
            break

        queue.append(current)

        step += 1
        if step > 5:
            step = 1

    print(f"#{t} {' '.join(map(str, list(queue)))}")