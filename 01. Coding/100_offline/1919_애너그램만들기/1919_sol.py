
"""
한 단어의 길이가 최대 1000자, 시간제한이 2초 (2억)이므로
for문 한 번 돌면? 1000
    두 번 돌면? 1000000 (백만) ------------------- > 최대 for문은 2번만 가능 
    세 번 돌면? 10000000000 (백억) -> 안됨

- 결국 공동으로 존재하는 단어들의 개수는 제외하고 나머지는 다 삭제하면 되니까 ..
"""

# input 받기
str1 = input()
str2 = input()

# 딕셔너리 초기화
str_dict = {}

cnt = 0

# str1을 돌면서 str_dict에 문자 개수 넣기
for letter in str1:
    if letter not in str_dict.keys():
        str_dict[letter] = 0

    str_dict[letter] += 1


# str2 돌면서 더합시당
for letter in str2:
    if letter in str_dict.keys():
        if str_dict[letter] > 0:
            str_dict[letter] -= 1
        else: # 0 이하이면 어쨌든 삭제해야하니까
            cnt += 1

    else: # 없으면
        cnt += 1

# 이거 시간복잡도가 늘어요 -> sum으로 갑시다요
# for key, value in str_dict.items():
#     if value != 0:
#         cnt += value


print(cnt + sum(list(str_dict.values())))