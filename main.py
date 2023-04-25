from tkinter import *
from tkinter import ttk

from program1 import program1
from program2 import program2
from program3 import program3
from program4 import program4

window = Tk()
window.title("программа")
window.geometry('1200x800')

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill=BOTH)

namesPrograms = ["program1",
                 "program2",
                 "program3",
                 "program4"]
frames = []

for i in range(4):
    frames.append(ttk.Frame(notebook))
    frames[i].pack(fill=BOTH, expand=True, padx=20, pady=20)
    notebook.add(frames[i], text=namesPrograms[i])

program1(window, frames[0])
program2(window, frames[1])
program3(window, frames[2])
program4(window, frames[3])

window.mainloop()
