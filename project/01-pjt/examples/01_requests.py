# 외부 라이브러리 requests를 import
import requests
from pprint import pprint # 좀 더 보기 쉽게 프린트해주고 이때 알파벳 순으로 정렬. 딕셔너리의 순서가 바뀐 것은 아님

# jsonplaceholder라고 하는 sample형 json 데이터 제공 API 활용
# requests는 get요청으로 응답받은 데이터를 담은 객체에게
# json()이라는 메서드를 만들어 두었다. -> JavaScript 형식의 JSON 데이터를
# 파이썬에서 사용할 수 있도록, 파이썬의 data type에 맞게 변환해주는 메서드
    # response.json()
response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response) # <Response [200]> : status_code (어떤 상황인지 알려주는 상태 코드)

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# print(response) # 전체 데이터 확인 가능

user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
# print(user_response)

# # 전체 데이터 순회하며 확인
# for item in response:
#     print(item)

completed_todos = []
fields = ['id', 'title']
# Completed가 True인 경우만 추출한다면?
for item in response:
    if item['completed']:
        # 그 중 내가 필요로 하는 2개의 필드 id, title만 따로 모은다.
        temp_item = {}
        for key in fields:
            temp_item[key] =item[key]

        for user in user_response:
            if user['id'] == item['userId']:
                # ctrl + alt + 위아래 방향키: 커서 복제
                # ctrl + shift + 좌우 방향키: 단어 단위로 드래그
                user_info = {
                    'id': user['id'],
                    'name':user['name'],
                    'username':user['username'],
                    'email': user['email']
                }
                temp_item['user'] = user_info
        completed_todos.append(temp_item)
pprint(completed_todos)

