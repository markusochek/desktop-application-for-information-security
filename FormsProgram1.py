from tkinter import *
from Program1 import get_mouse_symbol


def formsProgram1(window, frame):
    mouseEntry = Entry(frame)
    mouseEntry.grid(row=1, column=0)

    def entry_get_mouse_symbol():
        mouseEntry.insert(0, get_mouse_symbol())

    mouseButton = Button(
        frame,
        text='ввести буквы от движения мышки',
        command=entry_get_mouse_symbol
    )
    mouseButton.grid(row=2, column=0)