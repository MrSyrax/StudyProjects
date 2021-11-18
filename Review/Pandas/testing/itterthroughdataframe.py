import pandas
from tkinter import *
from tkinter import messagebox
# data = pandas.read_csv("Review/Pandas/weather_data.csv")

# new_dict = {index:row.day for (index,row) in data.iterrows()}

# new_list = [value for (index,value) in new_dict.items() if value[0] == 'S']

# print(new_list)

# rows_i_want = data.loc[data['day'].str.startswith('S')]

# print(rows_i_want)

window = Tk()
window.config(padx=50,pady=50, width=500,height=500)

def phonetic_word():
    choice = user_entery.get()
    phonetic_words = [phonetic_dict[n.upper()] for n in choice]
    messagebox.showinfo(title='word', message=phonetic_words)

data = pandas.read_csv('day26/nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

user_entery = Entry()
user_entery.grid(column=1,row=0)

enter_button = Button(text='Enter', command=phonetic_word)
enter_button.grid(padx=10, column=0,row=0)

window.mainloop()