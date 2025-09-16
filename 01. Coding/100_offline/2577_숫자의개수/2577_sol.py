"""
A * B * C 최악의 경우 997,002,999 -> 최대가 9자리라서 시간 제한 넉넉함
"""

num1, num2, num3 = int(input()), int(input()), int(input())
multipled = str(num1 * num2 * num3)
num_dict = {}

for i in range(10):
    num_dict[str(i)] = 0

for num in multipled:
     num_dict[num] += 1

for key, value in num_dict.items():
    print(value)