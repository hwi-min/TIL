import sys
sys.stdin = open('./SWEA_data_inputs/sample_input_4008.txt')

def calculate(num1, num2, command):
    if command == '+': return num1 + num2
    elif command == '-': return num1 - num2
    elif command == '*': return num1 * num2
    elif command == '//': return num1 // num2

def dfs(idx, current_sum):
    global command_lst, sum_set
    # command_lst의 마지막 인덱스 요소까지 탐색을 완료했다면
    if idx == len(command_lst):
        sum_set.add(current_sum) # sum_set에 현재까지의 값 추가
        return # 반환

    dfs(idx+1, current_sum+calculate())

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # 연산자 개수 저장
    plus, minus, multiple, division = map(int, input().strip().split())

    # 주어진 연산자 개수만큼 리스트로 만들기
    command_lst = ['+'] * plus + ['-'] * minus + ['*'] * multiple + ['//'] * division
    # 입력받은 숫자 저장 (숫자의 순서는 고정)
    nums = map(int, input().strip().split())
    # 연산끝낸 합을 저장할 Set 초기화
    sum_set = set()
    # 최대 최소 값 초기화
    max_num, min_num = float('inf'), float('-inf')

    # 연산자의 idx??
    dfs(idx, current_sum)







