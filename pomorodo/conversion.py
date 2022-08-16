from tkinter import *

# creating windows and setting title and dimesions
windows = Tk()
windows.title('Mile to KM converter')
windows.minsize(width=300, height=300)

# creating user input
entry = Entry(width=20)
entry.grid(row=1, column=2)

# creating the labels
miles_label = Label(text='Miles')
miles_label.grid(row=1, column=3)
km_label = Label(text='KM')
km_label.grid(row=2, column=3)
equal_label = Label(text='is equal to')
equal_label.grid(row=2, column=1)
number_label = Label(text='0')
number_label.grid(row=2, column=2)


# create button and the function
def convert_number():
    number = round(int(entry.get()) * 1.609344)
    number_label.config(text=number)


button = Button(text='Caculate', command=convert_number)
button.grid(row=3, column=2)

windows.mainloop()
