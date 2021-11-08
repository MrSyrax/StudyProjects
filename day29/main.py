from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website_entry.get()
    em = email_entry.get()
    pw = password_entry.get()
    with open('C:/Users/Kareyo/Documents/Python/StudyProjects/day29/credentials.txt', 'a') as file:
        file.write(f'{web} | {em} | {pw}\n')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file='C:/Users/Kareyo/Documents/Python/StudyProjects/day29/logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text='Website:')
website_label.grid(row=1,column=0)
email_lable = Label(text='Email/Username:')
email_lable.grid(row=2,column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.insert(END,'Kevincarrillo89@gmail.com')
email_entry.grid(row=2,column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(row=3,column=2)
add_button = Button(text='Add',width=44,command=save_data)
add_button.grid(row=4,column=1, columnspan=2)


window.mainloop()



