from functools import partial
from tkinter import *

from Program4 import fib_seq, fib_rand, fib_rand_all


def wrapper_fib_rand(frame, entries):
    seed1 = int(entries[0].get())
    seed2 = int(entries[1].get())
    primeNumber = int(entries[2].get())
    N = int(entries[3].get())

    result = fib_rand_all(seed1, seed2, primeNumber, N)

    Label(frame, text="result").grid(row=5, column=0)
    resultText = Text(frame)
    resultText.insert(1.0, result)
    resultText.grid(row=5, column=1)


def formsProgram4(window, frame):
    names = ["seed1",
             "seed2",
             "primeNumber",
             "N"]
    entries = []
    for i in range(4):
        Label(frame, text=names[i]).grid(row=i, column=0)
        entries.append(Entry(frame))
        entries[i].insert(0, '0')
        entries[i].grid(row=i, column=1)

    fibRandButton = Button(
        frame,
        text='fib_rand',
        command=partial(wrapper_fib_rand, frame, entries))
    fibRandButton.grid(row=4, column=1)
