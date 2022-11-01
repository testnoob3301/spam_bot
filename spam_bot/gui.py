from tkinter import *
from tkinter import ttk
import time

from setuptools import Command
import main
# main.stay_on_top
root = Tk()
root.geometry("300x200")
root.configure(bg="#4b4646")
root.title("Python chat bot")
label = ttk.Label(root, text='Press The buttton to start')
button = ttk.Button(root, text='Okay',command=main.run)
button1 = ttk.Button(root, text='lyric bomber',command=main.lyric)
button2 = ttk.Button(root, text='Merchant of venice',command=main.lyric_mov)
label.pack()
button.pack()
button1.pack()
button2.pack()
root.lift()
root.mainloop()