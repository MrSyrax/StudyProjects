from tkinter import *
calculation = 0

# #what the button does
# def button_clicked():
#     new_text=entry.get()
#     calculation = round(float(new_text)*1.609)
#     km_converted.config(text=f'{calculation}')

#create a window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=50,pady=30)


#create the labels
#create the miles label
miles = Label(text='Miles')
miles.grid(column=2,row=0)

#create the is equal to lablel
is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0,row=1)

#create the converted Lable
km_converted = Label(text='0')
km_converted.grid(column=1,row=1)

#create the KM label
km = Label(text='Km')
km.grid(column=2,row=1)

#create scale
def scale_used(value):
    x = round(float(value) * 1.609)
    km_converted.config(text=f'{x}')
   
scale = Scale(from_=100, to=0, command=scale_used)
scale.grid(column=1,row=2)


# #create the entry box
# entry = Entry(width=10)
# entry.grid(column=1,row=0)


# #create the buttoin
# button = Button(text='Calculate', command=button_clicked)
# button.grid(column=1,row=2)

window.mainloop()