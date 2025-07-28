"""
    외부 라이브러리나 모듈 등을 import 해와야 할 때,
    import가 반드시 필요한 경우에 받아 쓰기
"""
import requests
import csv

# jsonplaceholder라고 하는 sample형 json 데이터 제공 API 활용
# requests는 get요청으로 응답받은 데이터를 담은 객체에게
# json()이라는 메서드를 만들어 두었다. -> JavaScript 형식의 JSON 데이터를
# 파이썬에서 사용할 수 있도록, 파이썬의 data type에 맞게 변환해주는 메서드
    # response.json()
response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# print(response) # <Response [200]> : status_code (어떤 상황인지 알려주는 상태 코드)
completed_todos = []
fields = ['id', 'title']
for item in response:
    if item.get('completed'):
        temp_item = {}
        for key in fields:
            temp_item[key] =item[key]
        completed_todos.append(temp_item)

with open('completed_todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(completed_todos)