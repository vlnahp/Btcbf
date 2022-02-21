import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("Try code")
class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.write(str,False)
import sys
sys.stdout = StdoutRedirector(self)
entry = tkinter.Entry(root)
entry.pack()
print(entry.get())
def on_button():
    if entry.get() == "Screen" or entry.get() == "screen": #corrected
        slabel = tkinter.Label(root, text="Screen was entered")
        slabel.pack()
    else:
        tlabel = tkinter.Label(root, text="")
        tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()