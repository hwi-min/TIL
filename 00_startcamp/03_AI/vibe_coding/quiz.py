"""
quiz.py - ChatGPT API를 활용한 퀴즈 생성 모듈 (CLI용)
"""
import os
import openai
import json
import re

def generate_quiz_questions(title, summary, n=2):
    """
    기사 제목/요약을 바탕으로 ChatGPT(OpenAI API)로부터 퀴즈 n개(질문+모범답안) 리스트 반환
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")

    client = openai.OpenAI(api_key=api_key)

    prompt = (
        f"다음은 IT/AI 뉴스 기사입니다. 기사 내용을 바탕으로 독자가 기사 이해도를 점검할 수 있는 퀴즈 2개(질문과 모범답안)를 한국어로 만들어주세요.\n"
        f"\n[기사 제목]\n{title}\n\n[기사 요약]\n{summary}\n"
        "\n아래와 같은 JSON 리스트 형태로 반환하세요. 예시: [ {\"question\": \"질문1\", \"answer\": \"모범답안1\"}, ... ]\n"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.7,
    )
    content = response.choices[0].message.content
    match = re.search(r'\[.*\]', content, re.DOTALL)
    if not match:
        raise ValueError("ChatGPT 응답에서 퀴즈 JSON을 찾을 수 없습니다.\n응답: " + content)
    quiz_json = match.group(0)
    try:
        quiz_list = json.loads(quiz_json)
    except Exception as e:
        raise ValueError(f"퀴즈 JSON 파싱 오류: {e}\n원본: {quiz_json}")
    return quiz_list[:n]
