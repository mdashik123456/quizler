from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    
    def  __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.score_lable = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_lable.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text = "This is question", fill = THEME_COLOR, font = ("Arial", 20, "italic"))
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_lable.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz.\n\nYour final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
            
        
    def true_button(self):
        self.feedback(self.quiz.check_answer("True"))
        
    def false_button(self):
        self.feedback(self.quiz.check_answer("False"))
        
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
            
        self.window.after(1000, self.get_next_question)