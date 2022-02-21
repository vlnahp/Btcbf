import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = listBox.curselection()
	return itemSelected



root = Tk()

# This is the section of code which creates the main window
root.geometry('780x460')
root.configure(background='#FFFFFF')
root.title('Btcbf v1.2.1')


# This is the section of code which creates the a label
Label(root, text='Welcome to btcbf v1.2.1', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=59, y=74)


# This is the section of code which creates a listbox
listBox=Listbox(root, bg='#FFFFFF', font=('arial', 12, 'normal'), width=0, height=0)
a = listBox.curselection()
listBox.insert('0', '1: generate random key pair')
listBox.insert("1", '2: generate public address from private key')
listBox.insert('2', '3: brute force bitcoin offline mode')
listBox.insert('3', '4: brute force bitcoin online mode')
listBox.place(x=79, y=124)

def selected_item():
     
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    for i in listBox.curselection():
        if listBox.get(i) == "1: generate random key pair":
            print("31")
 
# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='Print Selected', command=selected_item)
btn.place(x=100, y=220) 

root.mainloop()
