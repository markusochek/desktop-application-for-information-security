from functools import partial
from tkinter import *

from Program1 import get_mouse_symbol


def entry_get_mouse_symbol(mouseEntry):
    mouseEntry.insert(0, get_mouse_symbol())


def formsProgram1(window, frame):
    mouseEntry = Entry(frame)
    mouseEntry.grid(row=1, column=0)

    mouseButton = Button(
        frame,
        text='ввести буквы от движения мышки',
        command=partial(entry_get_mouse_symbol, mouseEntry)
    )
    mouseButton.grid(row=2, column=0)
