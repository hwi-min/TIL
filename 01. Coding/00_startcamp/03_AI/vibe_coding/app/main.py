"""
앱 실행 진입점 (Flask/FastAPI/Django 중 Flask 예시)
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'IT/AI 트렌드 뉴스 추천 서비스'

if __name__ == '__main__':
    app.run(debug=True)
