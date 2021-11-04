from tkinter import *
calculation = 0

#what the button does
def button_clicked():
    new_text=entry.get()
    calculation = round(int(new_text)*1.6)
    km_converted.config(text=calculation)

#create a window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=50,pady=30)


#create the labels
miles = Label(text='Miles')
miles.grid(column=2,row=0)
is_equal_to = Label(text='is equal to ')
is_equal_to.grid(column=0,row=1)
km_converted = Label(text='0')
km_converted.grid(column=1,row=1)
km = Label(text='Km')
km.grid(column=2,row=1)

#create the entry box
entry = Entry(width=10)
entry.grid(column=1,row=0)


#create the buttoin
button = Button(text='Calculate', command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()









# #Button method
# def action():
#     label.config(text=entry.get())

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
# window.config(padx=20, pady=20)


# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.grid(column=0,row=0)
# label.config(padx=50,pady=50)


# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.grid(column=1,row=1)
# button2 = Button(text='New Button', command=action)
# button2.grid(column=2,row=0)

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.grid(column=3,row=2)

# window.mainloop()