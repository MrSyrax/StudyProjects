from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, width=400,height=400)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file='C:/Users/karey/Documents/Python/day29/logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.pack()

window.mainloop()



