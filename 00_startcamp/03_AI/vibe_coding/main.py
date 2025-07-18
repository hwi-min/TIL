"""
main.py - CLI 진입점
"""



import random
from news import fetch_latest_articles
from quiz import generate_quiz_questions

def main():
    print("\n[IT/AI 트렌드 뉴스 추천 CLI 서비스]")
    articles = fetch_latest_articles(5)
    if not articles:
        print("뉴스를 불러올 수 없습니다. 네트워크 상태를 확인하세요.")
        return
    # 오늘의 뉴스 1개 추천 (랜덤)
    today_news = random.choice(articles)
    print("\n오늘의 추천 뉴스!")
    print(f"\n제목: {today_news['title']}")
    print(f"출처: {today_news['source']}")
    print(f"요약: {today_news['summary'][:200]}...")
    print(f"링크: {today_news['link']}")

    input("\n기사를 다 읽으셨으면 Enter를 눌러주세요...")

    # 퀴즈 2개 생성 및 풀이
    quiz_list = generate_quiz_questions(today_news['title'], today_news['summary'])
    print("\n[기사 이해도 퀴즈]")
    score = 0
    for idx, quiz in enumerate(quiz_list, 1):
        print(f"\nQ{idx}. {quiz['question']}")
        user_answer = input("답변: ").strip()
        if user_answer:
            print(f"모범 답안: {quiz['answer']}")
        else:
            print("답변이 입력되지 않았습니다.")

if __name__ == "__main__":
    main()
