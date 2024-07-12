from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=tick_image, height=50, width=50, command=lambda answer="True": self.check_answer(answer))
        self.correct_btn.grid(row=2, column=0)

        cross_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=cross_image, height=50, width=50, command=lambda answer="False": self.check_answer(answer))
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text =  self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def check_answer(self, answer: str):
        is_right = self.quiz.check_answer(answer)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")

        self.window.after(1000, self.get_next_question)
