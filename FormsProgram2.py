from tkinter import *
from Program2 import lfsr_period

def formsProgram2(window, frame):
    Label(frame, text="Введите длину регистра 4 или 8: ").grid(row=0, column=0)
    registerLengthEntry = Entry(frame)
    registerLengthEntry.grid(row=0, column=1)
    n = int(registerLengthEntry.get())

    # for i in range(n):


    registerLengthButton = Button(
        frame,
        text='lfsr_period',
        command=lfsr_period
    )
    registerLengthButton.grid(row=1, column=1)

