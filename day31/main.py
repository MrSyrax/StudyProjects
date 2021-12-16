from tkinter import font
import pandas
from tkinter import *
from random import choice
import time


BACKGROUND_COLOR = "#B1DDC6"
random_word = {}


try:
    words = pandas.read_csv("C:/Users/karey/Documents/Python/day31/data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("C:/Users/karey/Documents/Python/day31/data/french_words.csv")
    word_dict = words.to_dict(orient='records')
else:
    word_dict = words.to_dict(orient='records')



def next_card():
    global random_word,flip_timer
    window.after_cancel(flip_timer)
    random_word = choice(word_dict)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=random_word['French'], fill='black')
    canvas.itemconfig(current_card, image=front_card)
    flip_timer = window.after(3000, flip_card)

def is_known():
    word_dict.remove(random_word)
    print(word_dict)
    data = pandas.DataFrame(word_dict)
    data.to_csv("C:/Users/karey/Documents/Python/day31/data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    global random_word
    canvas.itemconfig(current_card, image=back_card)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=random_word['English'],fill='white')

#create the window and config it
window = Tk()
window.title('Study Time')
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)

#VERY IMPORTANT - this will run a function after the specified time (in ms(miliseconds))
flip_timer = window.after(3000, flip_card)

#create canvas and place images on to it (flashards) and words
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="C:/Users/karey/Documents/Python/day31/images/card_front.png")
back_card = PhotoImage(file="C:/Users/karey/Documents/Python/day31/images/card_back.png")
current_card = canvas.create_image(400,263, image=front_card)
card_title = canvas.create_text(400,150,text='', font=('Ariel',40,'italic'))
card_word = canvas.create_text(400,263,text='', font=('Ariel',60,'bold'))
canvas.grid(column=0,row=0, columnspan=2)


#create the wrong button and set a picture for the button
wrong_button_image = PhotoImage(file="C:/Users/karey/Documents/Python/day31/images/wrong.png")
wrong_button = Button(image=wrong_button_image,highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="C:/Users/karey/Documents/Python/day31/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

next_card()


window.mainloop()