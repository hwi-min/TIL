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
    여러 IT/AI 뉴스 소스에서 최신 기사들을 수집하여 표준화된 리스트로 반환
    """
    articles = []
    for source in NEWS_SOURCES:
        feed = feedparser.parse(source['rss'])
        for entry in feed.entries[:max_articles]:
            articles.append({
                'source': source['name'],
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'summary': entry.get('summary', '')
            })
    return articles

if __name__ == "__main__":
    # 테스트: 기사 2개씩만 출력
    for article in fetch_latest_articles(2):
        print(f"[{article['source']}] {article['title']}\n{article['link']}\n{article['summary'][:100]}...\n")
