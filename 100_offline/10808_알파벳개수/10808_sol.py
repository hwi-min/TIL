"""
단어 최대 길이는 100, 시간제한은 1초 (1억)
for문 1번 -> 100
        2번 -> 10000
        3번 -> 1000000 
        4번 -> 100000000
"""

words = input()

word_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 
             'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for letter in words:
    word_dict[letter] += 1

for key, value in word_dict.items():
    print(value, end=' ')
