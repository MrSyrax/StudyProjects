from tkinter import *
from tkinter import messagebox
from typing import Counter

# window = Tk()
# window.config(padx=50,pady=50)

# def button_clicked():
#     writen_by_user = input.get()
#     label.config(text=writen_by_user)
#     input.delete(0,END)
#     messagebox.showinfo(title='user said', message=writen_by_user)
   

# label = Label(text='naisuhh')
# label.grid(column=0,row=0)

# button = Button(text='Click Me', command=button_clicked)
# button.grid(column=0,row=1)

# input = Entry(width=10)
# input.grid(column=1,row=1)

# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# button_radio = Radiobutton(text='Option 1',value=1, variable=radio_state, command=radio_used)
# button_radio.grid(column=1,row=2)

# button_radio2 = Radiobutton(text='Option 2',value=2, variable=radio_state, command=radio_used)


# window.mainloop()

window = Tk()
window.config(padx=50,pady=50,width=600,height=600)
window.title('WHAT EVER I LIKE BECUASE I PROGRAMMED THIS MOFUFA!')

def button_clicked():
    canvas.config(width=1024, height=1020)
    canvas.itemconfig(main_canvas,image=alpha_ultimate)
    canvas.itemconfig(text, text='Too late....')
    

canvas = Canvas(window, width=1024, height=1020)
alpha_pic = PhotoImage(file= "Review/tkinter/Coating-CrimsonAbyss-GenericFinal.png")
alpha_ultimate = PhotoImage(file="Review/tkinter/ultimate.png")
main_canvas = canvas.create_image(270,510, image=alpha_pic)
text = canvas.create_text(405,60,text='You are about to die!',font=('Ariel',20,'bold'),fill='red')
canvas.create_window(500,500)
canvas.grid(column=0,row=0)

button = Button(text='click me',command=button_clicked)
button.grid(column=1,row=0)


window.mainloop()