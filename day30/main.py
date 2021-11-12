from tkinter import messagebox
from tkinter import *

import pandas

# try:
#     my_dict = {'key': 'Value'}
#     user_input=input('please enter a name: ')
#     print(my_dict[user_input])
# except KeyError as r:
#     messagebox.showinfo(title='Oops', message=f"Looks like {r} isn't in the list")

window = Tk()

canvas = Canvas(width=800,height=800, bg='black', highlightthickness=0)
new_image = PhotoImage(file='C:/Users/karey/Documents/Python/day31/images/41XrfO3NugS._SR600,315_PIWhiteStrip,BottomLeft,0,35_SCLZZZZZZZ_FMpng_BG255,255,255.png')
canvas.create_image(400,400, image=new_image)
canvas.grid(column=0,row=0)

window.mainloop()

