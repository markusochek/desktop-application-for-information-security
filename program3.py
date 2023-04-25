# Линейный конгурэнтный метод
from functools import partial
from tkinter import *


def program3(window, frame):
    def linear_congruential_method(a, c, m, x0, n):
        result = []
        xi = x0
        for i in range(n):
            xi = (a * xi + c) % m
            result.append(xi)

        Label(frame, text="result").grid(row=6, column=0)
        resultEntry = Entry(frame)
        resultEntry.insert(0, str(result))
        resultEntry.grid(row=6, column=1)

        Label(frame, text="x0").grid(row=7, column=0)
        x0Entry = Entry(frame)
        x0Entry.insert(0, '0')
        x0Entry.grid(row=7, column=1)

        Label(frame, text="x1").grid(row=8, column=0)
        x1Entry = Entry(frame)
        x1Entry.insert(0, '0')
        x1Entry.grid(row=8, column=1)

        Label(frame, text="x2").grid(row=9, column=0)
        x2Entry = Entry(frame)
        x2Entry.insert(0, '0')
        x2Entry.grid(row=9, column=1)

        restoreSequenceButton = Button(
            frame,
            text='restore_sequence',
            command=partial(restore_sequence,
                            int(m),
                            x0Entry.get(),
                            x1Entry.get(),
                            x2Entry.get()))
        restoreSequenceButton.grid(row=10, column=1)

    names = ["введите a",
             "введите c",
             "введите m",
             "введите x0",
             "введите n"]
    entries = []

    for i in range(5):
        Label(frame, text=names[i]).grid(row=i, column=0)

        entries.append(Entry(frame))
        entries[i].insert(0, '0')
        entries[i].grid(row=i, column=1)

    linearButton = Button(
        frame,
        text='linear',
        command=partial(linear_congruential_method,
                        entries[0].get(),
                        entries[1].get(),
                        entries[2].get(),
                        entries[3].get(),
                        int(entries[4].get()))
    )
    linearButton.grid(row=5, column=1)

    # results = linear_congruential_method(1664525, 1013904223, 2 ** 32, 1, 10)

    # Взлом линейного конгурентного метода
    # a = 1664525
    # m = 2 ** 32
    # x0 = 1015568748
    # x1 = 1586005467
    # x2 = 2165703038

    def restore_sequence(m, x0, x1, x2):
        def f(m, x0, x1, x2):
            for a in range(0, (m)):
                if a * (x1 - x0) % (m) == (x2 - x1) % (m):
                    break
                else:
                    a = a + 1
                return a

        Label(frame, text="a").grid(row=11, column=0)
        aEntry = Entry(frame)
        aEntry.insert(0, str(f(m, x0, x1, x2)))
        aEntry.grid(row=11, column=1)
