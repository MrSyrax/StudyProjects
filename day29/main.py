from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_new_pw():
    #Password Generator Project
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for _ in range(randint(8, 10))]

    password_list+= [choice(symbols) for _ in range(randint(2, 4))]

    password_list+= [choice(numbers) for _ in range(randint(2, 4))]
   
    shuffle(password_list)

    password = ''.join(password_list)

    entry_field = password_entry.get()

    if len(entry_field) == 0:
        password_entry.insert(END,f'{password}')
        pyperclip.copy(password_entry.get())  
    else:
        password_entry.delete(0,END)
        password_entry.insert(END,f'{password}')
        pyperclip.copy(password_entry.get())
        pyperclip.paste()



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    web = website_entry.get().lower()
    em = email_entry.get()
    pw = password_entry.get()
    new_data = {
        web: {
            'email': em,
            'password': pw
            }
        }

    if len(web) == 0 or len(pw)== 0:
        messagebox.showinfo(title='Oops', message='Please do not leave any fields emtpy')
    else: 
        try:
            with open('C:/Users/karey/Documents/Python/day29/credentials.json', 'r') as file:
                #reading old data
                data = json.load(file)
                
        except FileNotFoundError:    
            with open('C:/Users/karey/Documents/Python/day29/credentials.json', 'w') as file:
                #saving the updated data
                json.dump(new_data, file, indent=4)
        else:
            #updating old data
            data.update(new_data)
            with open('C:/Users/karey/Documents/Python/day29/credentials.json', 'w') as file:
                #saving the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

# ---------------------------- SEARCH FOR CREDENTIALS ------------------------------- #

def search():
    web = website_entry.get().lower()
    if len(web)==0:
        messagebox.showinfo(title='Oops', message='no search given...')
    else:
        try:
            with open('C:/Users/karey/Documents/Python/day29/credentials.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title='Oops', message='No Data File Found.')
        else:
            if web not in data:
                messagebox.showinfo(title='Oops', message=f'There are no credentials for {web}.')
            else:
                user_name = data[web]['email']
                password = data[web]['password']
                messagebox.showinfo(title=web, message=f'Email: {user_name}\nPassword: {password}')







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file='C:/Users/karey/Documents/Python/day29/logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text='Website:')
website_label.grid(row=1,column=0)
email_lable = Label(text='Email/Username:')
email_lable.grid(row=2,column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

#creates the 'website entry with a width of 52
website_entry = Entry(width=33)
#places the website entry in row 1 column 1 with a columnspan of 2 (2 "cells")
website_entry.grid(row=1, column=1,)
#places the cursor on the website entry line
website_entry.focus()

email_entry = Entry(width=52)
#inserts "default text" into the entry line
email_entry.insert(END,'Kevincarrillo89@gmail.com')
email_entry.grid(row=2,column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

#creates the generate button with and it says "generate password" on the button
generate_password_button = Button(text='Generate Password', command=generate_new_pw)
generate_password_button.grid(row=3,column=2)

search_button = Button(text='Search', width=14, command=search)
search_button.grid(row=1,column=2)

add_button = Button(text='Add',width=44,command=save_data)
add_button.grid(row=4,column=1, columnspan=2)


window.mainloop()



