"""
다솜이의 방번호 N은 100만 

1. 다솜이의 방을 번호 숫자를 처음부터 하나씩 돌면서 확인
- False

"""
room_num = input()
check_list = [False]* len(room_num) # 방 번호 글자마다의 False 생성 [False] [False]
cnt = 0

for i in range(len(room_num)): # 0 idx ~
    num = room_num[i]

    if not check_list[num]: check_list[num] = True # True로 바꾸고
    else: # 이미 False야 그러면
        if num == 6 and not check_list[6]: check_list[6] = True
        elif num == 9 and not check_list[9]: check_list[9] = True
        else:
            cnt += 1
            check_list = [False] * (len(room_num))

print(cnt)