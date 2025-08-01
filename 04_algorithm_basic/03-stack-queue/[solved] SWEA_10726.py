import sys
sys.stdin = open('./SWEA_input_datas/input.txt')

T = int(input())

for t in range(1, T+1): 
    N,M = map(int, input().strip().split())
    binary = bin(M)[2:].zfill(N) # binary로 바꾼뒤 N자리 수가 되지 않는다면 0으로 채우기

    flag = True

    for i in range(len(binary)-1, len(binary)-N-1, -1): # 가장 뒤 index부터 -1씩 감소하며 N자리 확인
        if binary[i] != '1': # 1이 아니라면
            flag = False # flag=False로 바꾼 뒤 바로 return
            break

    print(f"#{t} {'OFF' if not flag else 'ON'}")