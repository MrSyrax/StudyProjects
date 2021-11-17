from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(padx=50,pady=50)

def button_clicked():
    writen_by_user = input.get()
    label.config(text=writen_by_user)
    input.delete(0,END)
    messagebox.showinfo(title='user said', message=writen_by_user)
   

label = Label(text='naisuhh')
label.grid(column=0,row=0)

button = Button(text='Click Me', command=button_clicked)
button.grid(column=0,row=1)

input = Entry(width=10)
input.grid(column=1,row=1)

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
button_radio = Radiobutton(text='Option 1',value=1, variable=radio_state, command=radio_used)
button_radio.grid(column=1,row=2)


window.mainloop()