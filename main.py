from tkinter import *
from tkinter import ttk

from FormsProgram1 import formsProgram1
from FormsProgram2 import formsProgram2
from FormsProgram3 import formsProgram3
from FormsProgram4 import formsProgram4

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

formsProgram1(window, frames[0])
formsProgram2(window, frames[1])
formsProgram3(window, frames[2])
formsProgram4(window, frames[3])

window.mainloop()
