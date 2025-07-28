import csv

# with open('users.csv', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content) # 모든 데이터가 한 번에 다 들어옴


## 리스트로 받기
# with open('users.csv', 'r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     # print(csv_reader) # 객체 자체가 반환됨
#     for row in csv_reader:
#         print(row)

## 딕셔너리로 받기
with open('users.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)

