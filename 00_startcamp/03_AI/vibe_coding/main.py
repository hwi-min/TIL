try:
    from gensim.summarization import summarize
except ImportError:
    summarize = None

def auto_summarize(text, ratio=0.2):
    if summarize is not None:
        try:
            result = summarize(text, ratio=ratio)
            if result:
                return result
        except Exception:
            pass
    return text[:500]  # 요약 실패 시 앞부분만
"""
main.py - CLI 진입점
"""





import random
import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser
from news import fetch_latest_articles
from quiz import generate_quiz_questions

BG_COLOR = "#f3f6fd"
CARD_COLOR = "#ffffff"
PRIMARY_COLOR = "#5a8dee"
ACCENT_COLOR = "#f7b731"
BTN_COLOR = "#5a8dee"
BTN_HOVER = "#3a6fd8"
BTN_TEXT_COLOR = "#fff"
SHADOW_COLOR = "#e0e6f7"
FONT_TITLE = ("Pretendard", 20, "bold")
FONT_LABEL = ("Pretendard", 12)
FONT_BOLD = ("Pretendard", 13, "bold")
FONT_BTN = ("Pretendard", 12, "bold")

class NewsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IT/AI 트렌드 뉴스 추천 GUI 서비스")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("800x650")
        self.articles = fetch_latest_articles(5)
        if not self.articles:
            messagebox.showerror("오류", "뉴스를 불러올 수 없습니다. 네트워크 상태를 확인하세요.")
            self.root.destroy()
            return
        self.today_news = random.choice(self.articles)
        self.quiz_list = []
        self.quiz_idx = 0
        self.score = 0
        self.create_news_frame()

    def create_news_frame(self):
        self.clear_frame()
        bg = tk.Frame(self.root, bg=BG_COLOR)
        bg.pack(fill='both', expand=True)
        # 카드 프레임
        card = tk.Frame(bg, bg=CARD_COLOR, bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor='center', width=700, height=540)
        # 그림자 효과
        shadow = tk.Frame(bg, bg=SHADOW_COLOR, bd=0, highlightthickness=0)
        shadow.place(relx=0.5, rely=0.5, anchor='center', width=710, height=550)
        shadow.lower(card)

        tk.Label(card, text="오늘의 추천 뉴스", font=FONT_TITLE, bg=CARD_COLOR, fg=PRIMARY_COLOR).pack(pady=(18, 10))
        tk.Label(card, text=self.today_news['title'], font=(FONT_BOLD[0], 18, "bold"), bg=CARD_COLOR, fg="#222", wraplength=600, justify='left').pack(anchor='w', padx=36, pady=(0, 8))
        tk.Label(card, text=f"출처: {self.today_news['source']}", font=FONT_LABEL, bg=CARD_COLOR, fg="#888").pack(anchor='w', padx=36, pady=(0, 10))

        # 요약 영역
        summary_row = tk.Frame(card, bg=CARD_COLOR)
        summary_row.pack(anchor='w', padx=30, pady=(0, 2))
        tk.Label(summary_row, text="요약", font=FONT_BOLD, bg=CARD_COLOR, fg=ACCENT_COLOR).pack(side='left')
        tk.Label(summary_row, text="자동 요약", font=(FONT_LABEL[0], 10, "bold"), bg="#e0e6f7", fg=PRIMARY_COLOR, padx=8, pady=2, relief='flat', bd=0).pack(side='left', padx=(8,0))

        news_content = self.today_news.get('content') or self.today_news.get('summary', '')
        summary_text = auto_summarize(news_content)
        summary_frame = tk.Frame(card, bg=CARD_COLOR)
        summary_frame.pack(anchor='w', padx=30, pady=(0, 14), fill='x')
        summary_box = scrolledtext.ScrolledText(summary_frame, height=10, width=80, wrap='word', font=FONT_LABEL, bg="#f8faff", relief='flat', bd=0, padx=16, pady=8)
        summary_box.insert(tk.END, summary_text)
        summary_box.config(state='disabled')
        summary_box.pack(fill='x', expand=True)

        # 기사 원문 버튼
        link_btn = tk.Button(card, text="기사 원문 보기", font=FONT_BTN, bg="#e0e6f7", fg=PRIMARY_COLOR, activebackground="#d0d6e7", activeforeground=PRIMARY_COLOR, relief='flat', padx=14, pady=6, bd=0, cursor="hand2", command=lambda: webbrowser.open(self.today_news['link']))
        link_btn.pack(anchor='e', padx=36, pady=(0, 18))
        link_btn.bind('<Enter>', lambda e: link_btn.config(bg="#d0d6e7"))
        link_btn.bind('<Leave>', lambda e: link_btn.config(bg="#e0e6f7"))

        btn_frame = tk.Frame(card, bg=CARD_COLOR)
        btn_frame.pack(pady=(10, 0))
        other_btn = tk.Button(btn_frame, text="다른 뉴스 추천", font=FONT_BTN, bg="#e0e6f7", fg=PRIMARY_COLOR, activebackground="#d0d6e7", activeforeground=PRIMARY_COLOR, relief='flat', padx=12, pady=8, command=self.recommend_another_news, bd=0)
        other_btn.pack(side='left', padx=(0, 20))
        other_btn.bind('<Enter>', lambda e: other_btn.config(bg="#d0d6e7"))
        other_btn.bind('<Leave>', lambda e: other_btn.config(bg="#e0e6f7"))
        quiz_btn = tk.Button(btn_frame, text="기사를 다 읽었습니다! 퀴즈 풀기 →", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=BTN_HOVER, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=16, pady=8, command=self.start_quiz, bd=0)
        quiz_btn.pack(side='left')
        quiz_btn.bind('<Enter>', lambda e: quiz_btn.config(bg=BTN_HOVER))
        quiz_btn.bind('<Leave>', lambda e: quiz_btn.config(bg=BTN_COLOR))
        card.after(100, lambda: card.tkraise())
        self.current_frame = bg

    def recommend_another_news(self):
        # 현재 기사 제외한 다른 기사 중에서 랜덤 추천
        if len(self.articles) > 1:
            others = [a for a in self.articles if a != self.today_news]
            import random
            self.today_news = random.choice(others)
            self.quiz_list = []
            self.quiz_idx = 0
            self.score = 0
            self.create_news_frame()
        else:
            messagebox.showinfo("알림", "추천 가능한 다른 뉴스가 없습니다.")

    def new_recommendation(self):
        self.articles = fetch_latest_articles(5)
        if not self.articles:
            messagebox.showerror("오류", "뉴스를 불러올 수 없습니다. 네트워크 상태를 확인하세요.")
            self.root.destroy()
            return
        self.today_news = random.choice(self.articles)
        self.quiz_list = []
        self.quiz_idx = 0
        self.score = 0
        self.create_news_frame()

    def start_quiz(self):
        self.quiz_list = generate_quiz_questions(self.today_news['title'], self.today_news['summary'])
        self.quiz_idx = 0
        self.score = 0
        self.show_quiz()

    def show_quiz(self):
        self.clear_frame()
        bg = tk.Frame(self.root, bg=BG_COLOR)
        bg.pack(fill='both', expand=True)
        card = tk.Frame(bg, bg=CARD_COLOR, bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor='center', width=700, height=340)
        shadow = tk.Frame(bg, bg=SHADOW_COLOR, bd=0, highlightthickness=0)
        shadow.place(relx=0.5, rely=0.5, anchor='center', width=710, height=350)
        shadow.lower(card)
        if self.quiz_idx < len(self.quiz_list):
            quiz = self.quiz_list[self.quiz_idx]
            tk.Label(card, text=f"Q{self.quiz_idx+1}.", font=FONT_BOLD, bg=CARD_COLOR, fg=PRIMARY_COLOR).pack(anchor='w', padx=30, pady=(24, 0))
            tk.Label(card, text=quiz['question'], font=FONT_BOLD, bg=CARD_COLOR, wraplength=420, justify='left').pack(anchor='w', padx=30, pady=(0, 12))
            self.answer_entry = tk.Entry(card, font=FONT_LABEL, width=70, relief='flat', bd=0, bg="#f8faff", fg="#222")
            self.answer_entry.pack(pady=(0, 10), ipady=7, padx=30)
            self.answer_entry.insert(0, "여기에 답변을 입력하세요...")
            def clear_placeholder(e):
                if self.answer_entry.get() == "여기에 답변을 입력하세요...":
                    self.answer_entry.delete(0, tk.END)
                    self.answer_entry.config(fg="#222")
            self.answer_entry.bind('<FocusIn>', clear_placeholder)
            btn = tk.Button(card, text="제출", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=BTN_HOVER, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=12, pady=6, command=self.check_answer, bd=0)
            btn.pack(pady=(0, 10))
            btn.bind('<Enter>', lambda e: btn.config(bg=BTN_HOVER))
            btn.bind('<Leave>', lambda e: btn.config(bg=BTN_COLOR))
            self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        else:
            tk.Label(card, text="퀴즈가 모두 끝났습니다!", font=FONT_TITLE, bg=CARD_COLOR, fg=PRIMARY_COLOR).pack(pady=(40, 18))
            again_btn = tk.Button(card, text="다시 뉴스 추천 받기", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=BTN_HOVER, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=16, pady=8, command=self.new_recommendation, bd=0)
            again_btn.pack(pady=(0, 10))
            again_btn.bind('<Enter>', lambda e: again_btn.config(bg=BTN_HOVER))
            again_btn.bind('<Leave>', lambda e: again_btn.config(bg=BTN_COLOR))
        card.after(100, lambda: card.tkraise())
        self.current_frame = bg

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        quiz = self.quiz_list[self.quiz_idx]
        answer_msg = f"모범 답안: {quiz['answer']}"
        if not user_answer:
            self.show_custom_popup("알림", "답변이 입력되지 않았습니다.\n" + answer_msg)
        else:
            self.show_custom_popup("정답 확인", answer_msg)

    def show_custom_popup(self, title, message):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.configure(bg=BG_COLOR)
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()
        popup.update_idletasks()
        w, h = 500, 240
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (w // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (h // 2)
        # 카드+그림자
        shadow = tk.Frame(popup, bg=SHADOW_COLOR, bd=0, highlightthickness=0)
        shadow.place(relx=0.5, rely=0.5, anchor='center', width=w+10, height=h+10)
        card = tk.Frame(popup, bg=CARD_COLOR, bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor='center', width=w, height=h)
        shadow.lower(card)
        tk.Label(card, text=title, font=("Pretendard", 15, "bold"), fg=PRIMARY_COLOR, bg=CARD_COLOR).pack(pady=(24, 8))
        tk.Label(card, text=message, font=FONT_LABEL, bg=CARD_COLOR, wraplength=320, justify='center').pack(pady=(0, 18))
        close_btn = tk.Button(card, text="확인", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=BTN_HOVER, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=16, pady=6, command=lambda: self._close_popup_and_next(popup), bd=0)
        close_btn.pack()
        close_btn.bind('<Enter>', lambda e: close_btn.config(bg=BTN_HOVER))
        close_btn.bind('<Leave>', lambda e: close_btn.config(bg=BTN_COLOR))
        popup.bind('<Return>', lambda e: self._close_popup_and_next(popup))
        close_btn.focus_set()

    def _close_popup_and_next(self, popup):
        popup.destroy()
        self.quiz_idx += 1
        self.show_quiz()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        quiz = self.quiz_list[self.quiz_idx]
        answer_msg = f"모범 답안: {quiz['answer']}"
        if not user_answer:
            messagebox.showinfo("알림", "답변이 입력되지 않았습니다.\n" + answer_msg)
        else:
            messagebox.showinfo("정답 확인", answer_msg)
        self.quiz_idx += 1
        self.show_quiz()

    def clear_frame(self):
        if hasattr(self, 'current_frame') and self.current_frame:
            self.current_frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewsQuizApp(root)
    root.mainloop()
