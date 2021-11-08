from os import terminal_size
from tkinter import *
from tkinter import font
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- set study time ------------------------------- # 

def spinbox_used():
    global WORK_MIN
    #gets the current value in spinbox.
    WORK_MIN = int(spinbox.get())

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    check_marks.config(text='')
    title_label.config(text='Timer',fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    if reps % 2 == 0:
        title_label.config(text='Break',fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        title_label.config(text='Break',fg=RED)
        count_down(long_break_sec)
    else:
        title_label.config(text='WORK!',fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    global reps

    if count_min < 10:
        count_min = f'0{count_min}'

    if count_min == 0:
        count_min = "00"
        
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_sec == 0:
        count_sec = "00"


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks+= '✔'
        check_marks.config(text=marks)

    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Study Time')
window.config(padx=100,pady=50,bg=YELLOW)

#Create lables check marks and timer lable 
title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME,50,'bold'))
title_label.grid(column=1,row=0)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=4)


#create canvas where the tomato picture will go
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='C:/Users/Karey/Documents/Python/day28/tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text='00:00', fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

#create the buttons "start" and "reset"
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

spinbox = Spinbox(from_=0, to=60, width=5, command=spinbox_used)
spinbox.grid(column=3,row=0)

window.mainloop()