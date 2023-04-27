from functools import partial
from tkinter import *

import FormsProgram2
from Program2 import lfsr_period, solve_mod_2

registerLengthSelectionButton = None


def parse(n, AEntry):
    A = AEntry.get()
    ANew = []
    for i in range(len(A)):
        if (A[i] == '1') or (A[i] == '0'):
            ANew.append(int(A[i]))
    print(ANew)

    AnewLine = []
    stream = []
    j = 0
    for i in range(len(ANew)):
        if j != n:
            j = j + 1
        else:
            AnewLine.append(stream)
            j = 1
            stream = []
        stream.append(ANew[i])
    AnewLine.append(stream)

    if len(AnewLine) == 1:
        AnewLine = AnewLine[0]

    return AnewLine


def wrapper_solve_mod_2(frame, n, AEntry, BEntry):
    A = parse(n, AEntry)
    B = parse(n, BEntry)

    x = solve_mod_2(A, B)
    Label(frame, text="x: ").grid(row=n + 9, column=0)
    iEntry = Entry(frame)
    iEntry.insert(0, x)
    iEntry.grid(row=n + 9, column=1)


def register_length_selection(frame, registerLengthEntry):
    for widget in frame.winfo_children():
        if widget != registerLengthEntry and widget != FormsProgram2.registerLengthSelectionButton:
            widget.destroy()
    n = int(registerLengthEntry.get())
    entries = []
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
    linesText = Text(frame)
    linesText.insert(1.0, elements[1])
    linesText.grid(row=n + 5, column=1)

    Label(frame, text="введите A: ").grid(row=n + 6, column=0)
    AEntry = Entry(frame)
    AEntry.grid(row=n + 6, column=1)

    Label(frame, text="введите B: ").grid(row=n + 7, column=0)
    BEntry = Entry(frame)
    BEntry.grid(row=n + 7, column=1)

    solveMod2Button = Button(
        frame,
        text='solve_mod_2',
        command=partial(wrapper_solve_mod_2, frame, n, AEntry, BEntry)
    )
    solveMod2Button.grid(row=n + 8, column=1)


def formsProgram2(window, frame):
    Label(frame, text="Введите длину регистра 4 или 8: ").grid(row=0, column=0)
    registerLengthEntry = Entry(frame)
    registerLengthEntry.insert(0, '4')
    registerLengthEntry.grid(row=0, column=1)

    FormsProgram2.registerLengthSelectionButton = Button(
        frame,
        text='register_length_selection',
        command=partial(register_length_selection, frame, registerLengthEntry)
    )
    FormsProgram2.registerLengthSelectionButton.grid(row=1, column=1)
