from functools import partial
from tkinter import *
from Program2 import lfsr_period


def register_length_selection(frame, registerLengthEntry):
    n = int(registerLengthEntry.get())
    entries = []
    print(n)
    for i in range(n):
        Label(frame, text="Введите значение " + str(i + 1) + ": ").grid(row=i + 2, column=0)
        entries.append(Entry(frame))
        entries[i].grid(row=i + 2, column=1)

    lfsrPeriodButton = Button(
        frame,
        text='lfsr_period',
        command=partial(wrapper_lfsr_period, frame, n, entries)
    )
    lfsrPeriodButton.grid(row=n + 3, column=1)


def wrapper_lfsr_period(frame, n, entries):
    ivr = []
    for i in range(n):
        ivr.append(int(entries[i].get()))
    elements = lfsr_period(n, ivr)

    Label(frame, text="период равен: ").grid(row=n + 4, column=0)
    iEntry = Entry(frame)
    iEntry.insert(0, elements[0])
    iEntry.grid(row=n + 4, column=1)

    Label(frame, text="lines: ").grid(row=n + 5, column=0)
    iText = Text(frame)
    iText.insert(1.0, elements[1])
    iText.grid(row=n + 5, column=1)


def formsProgram2(window, frame):
    Label(frame, text="Введите длину регистра 4 или 8: ").grid(row=0, column=0)
    registerLengthEntry = Entry(frame)
    registerLengthEntry.insert(0, '4')
    registerLengthEntry.grid(row=0, column=1)

    registerLengthSelectionButton = Button(
        frame,
        text='register_length_selection',
        command=partial(register_length_selection, frame, registerLengthEntry)
    )
    registerLengthSelectionButton.grid(row=1, column=1)
