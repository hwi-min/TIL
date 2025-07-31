import sys

sys.stdin = open('./SWEA_input_datas/input.txt')

from itertools import permutations

# 카드가 run인지 확인
def is_run(cards):
    return int(cards[0]) + 1 == int(cards[1]) and int(cards[1]) + 1 == int(cards[2])
# 카드가 triplet인지 확인
def is_triplet(cards):
    return cards[0] == cards[1] == cards[2]
# run과 triplet으로만 구성되어있는지 확인
def is_babygin_permutations(cards):
    if len(cards) != 6:
        return False
    # 가능한 모든 순열 생성
    for perm in permutations(cards):
        first_group = perm[:3]
        second_group = perm[3:]

        # 두 그룹이 모두 run이거나 triplet인 경우 True
        if (is_run(first_group) or is_triplet(first_group)) and \
                (is_run(second_group) or is_triplet(second_group)):
            return True

    return False

T = int(input())
for t in range(1, T+1):
    cards = input().strip()
    result = 'true' if is_babygin_permutations(cards) else 'false'
    print(f"#{t} {result}")