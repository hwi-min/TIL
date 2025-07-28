import requests

# TMDB API 키 설정
API_KEY = 'a32313cfc5ff2fbb1db057e1d6de12bf'
# BASE_URL = 'https://api.themoviedb.org/3'



# # API 호출 함수
# def get_popular_movies(page=1):
#     url = f'{BASE_URL}/'

import requests

url = "https://api.themoviedb.org/3/account/22172568/favorite/movies?language=en-US&page=1&sort_by=created_at.asc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer <ACCESS_TOKEN>"
}

response = requests.get(url, headers=headers)

print(response.text)


# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

