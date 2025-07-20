"""
news.py - IT/AI 뉴스 수집 및 표준화 모듈 (CLI용)
"""
import feedparser

NEWS_SOURCES = [
    {
        'name': 'AI타임즈',
        'rss': 'https://www.aitimes.com/rss/allArticle.xml'
    },
    {
        'name': '블로터',
        'rss': 'https://www.bloter.net/rss'
    },
    {
        'name': 'ITWorld Korea',
        'rss': 'https://www.itworld.co.kr/news/rss'
    },
]

def fetch_latest_articles(max_articles=5):
    """
    여러 IT/AI 뉴스 소스에서 최신 기사 중 AI 관련 키워드가 포함된 기사만 표준화된 리스트로 반환
    """
    AI_KEYWORDS = ["ai", "인공지능", "챗봇", "딥러닝", "머신러닝", "생성형", "chatgpt", "gpt", "llm", '데이터', 'data', 'gemeni']
    articles = []
    for source in NEWS_SOURCES:
        feed = feedparser.parse(source['rss'])
        for entry in feed.entries[:max_articles*2]:  # 필터링을 위해 더 많이 가져옴
            title = entry.get('title', '')
            summary = entry.get('summary', '')
            text = (title + ' ' + summary).lower()
            if any(keyword in text for keyword in AI_KEYWORDS):
                articles.append({
                    'source': source['name'],
                    'title': title,
                    'link': entry.get('link', ''),
                    'summary': summary
                })
                if len(articles) >= max_articles:
                    break
        if len(articles) >= max_articles:
            break
    return articles

if __name__ == "__main__":
    # 테스트: 기사 2개씩만 출력
    for article in fetch_latest_articles(2):
        print(f"[{article['source']}] {article['title']}\n{article['link']}\n{article['summary'][:100]}...\n")
