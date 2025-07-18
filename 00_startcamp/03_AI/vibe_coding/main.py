"""
main.py - CLI 진입점
"""





import random
import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser
from news import fetch_latest_articles
from quiz import generate_quiz_questions

BG_COLOR = "#f7f7fa"
PRIMARY_COLOR = "#4f8cff"
BTN_COLOR = "#4f8cff"
BTN_TEXT_COLOR = "#fff"
FONT_TITLE = ("Malgun Gothic", 18, "bold")
FONT_LABEL = ("Malgun Gothic", 12)
FONT_BOLD = ("Malgun Gothic", 12, "bold")
FONT_BTN = ("Malgun Gothic", 11, "bold")

class NewsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IT/AI 트렌드 뉴스 추천 GUI 서비스")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("600x500")
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
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(padx=30, pady=30, fill='both', expand=True)

        tk.Label(frame, text="오늘의 추천 뉴스!", font=FONT_TITLE, bg=BG_COLOR, fg=PRIMARY_COLOR).pack(pady=(0, 18))
        tk.Label(frame, text=f"제목: {self.today_news['title']}", font=FONT_BOLD, bg=BG_COLOR, wraplength=540, justify='left').pack(anchor='w', pady=(0, 6))
        tk.Label(frame, text=f"출처: {self.today_news['source']}", font=FONT_LABEL, bg=BG_COLOR, fg="#888").pack(anchor='w', pady=(0, 6))

        tk.Label(frame, text="요약:", font=FONT_BOLD, bg=BG_COLOR).pack(anchor='w', pady=(0, 2))
        summary_box = scrolledtext.ScrolledText(frame, height=7, width=70, wrap='word', font=FONT_LABEL, bg="#fff", relief='solid', bd=1)
        summary_box.insert(tk.END, self.today_news['summary'])
        summary_box.config(state='disabled')
        summary_box.pack(anchor='w', pady=(0, 10), fill='x')

        link_label = tk.Label(frame, text=f"기사 원문 보기", font=FONT_LABEL, fg=PRIMARY_COLOR, bg=BG_COLOR, cursor="hand2", underline=True)
        link_label.pack(anchor='w', pady=(0, 18))
        link_label.bind("<Button-1>", lambda e: webbrowser.open(self.today_news['link']))

        tk.Button(frame, text="기사를 다 읽었습니다! 퀴즈 풀기 →", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=PRIMARY_COLOR, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=16, pady=8, command=self.start_quiz).pack(pady=(10, 0))
        self.current_frame = frame

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
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(padx=30, pady=30, fill='both', expand=True)
        if self.quiz_idx < len(self.quiz_list):
            quiz = self.quiz_list[self.quiz_idx]
            tk.Label(frame, text=f"Q{self.quiz_idx+1}. {quiz['question']}", font=FONT_BOLD, bg=BG_COLOR, wraplength=540, justify='left').pack(anchor='w', pady=(0, 12))
            self.answer_entry = tk.Entry(frame, font=FONT_LABEL, width=60, relief='solid', bd=1)
            self.answer_entry.pack(pady=(0, 10), ipady=5)
            btn = tk.Button(frame, text="제출", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=PRIMARY_COLOR, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=12, pady=6, command=self.check_answer)
            btn.pack(pady=(0, 10))
            self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        else:
            tk.Label(frame, text="퀴즈가 모두 끝났습니다!", font=FONT_TITLE, bg=BG_COLOR, fg=PRIMARY_COLOR).pack(pady=(0, 18))
            tk.Button(frame, text="다시 뉴스 추천 받기", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=PRIMARY_COLOR, activeforeground=BTN_TEXT_COLOR, relief='flat', padx=16, pady=8, command=self.new_recommendation).pack(pady=(0, 10))
        self.current_frame = frame

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
