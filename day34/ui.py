import html
from tkinter import *
from tkinter import font
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        #create and configure the window and title it Quizzler
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #create the score label
        self.label = self.score = Label(self.window, text=f'Score: 0')
        self.score.config(fg='white',bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        #create the canvas where the question will go
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280 ,
            text='oooh mama',
            font=('Arial',20,'italic'),
            fill=THEME_COLOR
            )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        #Create false button
        self.false_button_img = PhotoImage(file='day34/images/false.png')
        self.false_button = Button(image=self.false_button_img, highlightthickness=0,command=self.wrong_answer)
        self.false_button.config(pady=50,padx=50)
        self.false_button.grid(column=1,row=2)
        
        #create true button
        self.true_button_img = PhotoImage(file='day34/images/true.png')
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=self.right_answer)
        self.true_button.config(pady=50,padx=50)
        self.true_button.grid(column=0,row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, text=q_text)


    def wrong_answer(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg='green')
            self.label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)    
        

    def right_answer(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg='green')
            self.label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000,self.get_next_question)
        
        
