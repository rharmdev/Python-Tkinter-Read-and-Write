from tkinter import *
import tkinter as tk
import os


def OnPressed1(event):
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    x4 = int(x1) + int(x2) + int(x3)
    Lab = Label(text=x4, background = "grey")
    Lab.pack()
    def write():
        file = open("numbers.txt", "w")
        file.write(str(x1))
        file.write(",")
        file.write(str(x2))
        file.write(",")
        file.write(str(x3))
        file.write(",")
        file.write(str(x4))
        file.close
        os.startfile("numbers.txt", 'open')
    But2 = Button(text= "Would you like to save this information? Click for yes. ", command = write, background = "grey")
    But2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    

root = tk.Tk()
root.title("R/W")
root.resizable(False, False)
root.geometry("450x180")
root.configure(background = "grey")
entry1 = tk.Entry (root, border = 5)
entry1.place(x=0, y=0)
entry2 = tk.Entry (root, border = 5)
entry2.place(x=150, y=0)
entry3 = tk.Entry (root, border = 5)
entry3.place(x=300, y=0)


But1 = Button(root, text= "Enter 3 Numbers and click", border=2, fg="black")
But1.place(relx=0.5, rely=0.5, anchor=CENTER)
But1.bind('<Button-1>', OnPressed1)
root.mainloop()

