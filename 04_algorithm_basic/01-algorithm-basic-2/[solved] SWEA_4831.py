import sys
sys.stdin = open('./SWEA_input_datas/sample_input_4831.txt')

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split()) # 한번에 갈 수 있는 수, 종점, 충전소 개수
    stops = list(map(int, input().split()))
    street_lst = []

    # 충전소가 없으면 0, 있으면 1, 도착지점이면 2
    for i in range(N+1):
        if i in stops: street_lst.append(1)
        elif i == N: street_lst.append(2)
        else: street_lst.append(0)

    charget_cnt = 0
    steps = K

    while bus_pos < N: # 종점
        for i in range(bus_pos + 1, bus_pos + K +1):
            if i > N:
                break
            if street_lst[i] == 1:
                last_stop = i

    print(K, N, M, stops, street_lst)

