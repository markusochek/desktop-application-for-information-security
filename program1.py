# Генератор последовательности от движения мышки
from functools import partial
from tkinter import *
import ctypes
import time


def program1(window, frame):
    # timerLabel = Label(frame)
    # timerLabel.grid(row=0, column=0)

    mouseEntry = Entry(frame)
    mouseEntry.grid(row=1, column=0)

    def print_mouse_symbol(mouseEntry):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

        for i in range(20):
            point = POINT()
            ctypes.windll.user32.GetCursorPos(ctypes.pointer(point))
            time.sleep(0.2)
            symbol = (point.x % 90 ** point.y % 90) % 90 + 33

            # timerLabel["text"] = str(20-i)
            mouseEntry.insert(0, chr(symbol))

    mouseButton = Button(
        frame,
        text='ввести буквы от движения мышки',
        command=partial(print_mouse_symbol, mouseEntry)
    )
    mouseButton.grid(row=2, column=0)
