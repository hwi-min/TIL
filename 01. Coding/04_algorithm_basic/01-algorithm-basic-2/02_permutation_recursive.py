
def perm(selected, remain):
    '''
    Args:
        selected: 선택된 값 목록
        reamin: 선택되지 않고 남은 값 목록 
    '''
    # 모든 요소를 선택할 것이니, 나머지가 없을 때까지 선택
    # if len(remain) == 3: # 선택한 것을 쓸 것인지, 남은 것을 쓸 것인지는 선택
    # if not remain:
    if not remain:
        print(*selected)
    else: # 아직 선택할 수 있는 요소들이 남아 있다면!
        for idx in range(len(remain)): # 그 요소를 모두 순회하면서
            # idx번째의 요소를 선택
            selected_item = remain[idx]
            # 선택된 idx번째를 제외한 remain을 만들자
            remain_list = remain[:idx] + remain[idx+1:]
            perm(selected + [selected_item], remain_list)



# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
