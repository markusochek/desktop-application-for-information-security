from functools import partial
from tkinter import *

from Program3 import linear_congruential_method, restore_sequence


def wrapper_restore_sequence(frame, m, entries):
    x0 = int(entries[0].get())
    x1 = int(entries[1].get())
    x2 = int(entries[2].get())
    elements = restore_sequence(m, x0, x1, x2)

    Label(frame, text="a").grid(row=10, column=0)
    aEntry = Entry(frame)
    aEntry.insert(0, str(elements[0]))
    aEntry.grid(row=10, column=1)

    Label(frame, text="c").grid(row=11, column=0)
    cEntry = Entry(frame)
    cEntry.insert(0, str(elements[1]))
    cEntry.grid(row=11, column=1)


def wrapper_linear_congruential_method(frame, entries):
    m = 2 ** 32
    a = int(entries[0].get())
    c = int(entries[1].get())
    x0 = int(entries[2].get())
    n = int(entries[3].get())
    result = linear_congruential_method(a, c, m, x0, n)

    Label(frame, text="result: ").grid(row=5, column=0)
    resultText = Text(frame)
    resultText.insert(1.0, result)
    resultText.grid(row=5, column=1)

    names = ["x0",
             "x1",
             "x2"]
    entries = []
    for i in range(3):
        Label(frame, text=names[i]).grid(row=i + 6, column=0)
        entries.append(Entry(frame))
        entries[i].insert(0, '0')
        entries[i].grid(row=i + 6, column=1)

    restoreSequenceButton = Button(
        frame,
        text='restore_sequence',
        command=partial(wrapper_restore_sequence, frame, m, entries)
    )
    restoreSequenceButton.grid(row=9, column=1)


def formsProgram3(window, frame):
    names = ["введите a: ",
             "введите c: ",
             "введите x0: ",
             "введите n: "]
    entries = []

    for i in range(4):
        Label(frame, text=names[i]).grid(row=i, column=0)
        entries.append(Entry(frame))
        entries[i].insert(0, '0')
        entries[i].grid(row=i, column=1)

    linearButton = Button(
        frame,
        text='linear',
        command=partial(wrapper_linear_congruential_method, frame, entries)
    )
    linearButton.grid(row=4, column=1)
