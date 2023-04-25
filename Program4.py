# Метод фибоначи с запаздыванием
from functools import partial
from tkinter import *


def program4(window, frame):
    Label(frame, text="seed1").grid(row=0, column=0)
    seed1Entry = Entry(frame)
    seed1Entry.insert(0, '0')
    seed1Entry.grid(row=0, column=1)

    Label(frame, text="seed2").grid(row=1, column=0)
    seed2Entry = Entry(frame)
    seed2Entry.insert(0, '0')
    seed2Entry.grid(row=1, column=1)

    Label(frame, text="primeNumber").grid(row=2, column=0)
    primeNumberEntry = Entry(frame)
    primeNumberEntry.insert(0, '0')
    primeNumberEntry.grid(row=2, column=1)

    Label(frame, text="N").grid(row=3, column=0)
    NEntry = Entry(frame)
    NEntry.insert(0, '0')
    NEntry.grid(row=3, column=1)

    def fib_seq(seed1, seed2):
        a, b = seed1, seed2
        while True:
            yield a
            a, b = b, a + b

    def fib_rand(seed1, seed2, prime_number, n):
        fib_gen = fib_seq(seed1, seed2)
        nums = []
        for i in range(n):
            nums.append(next(fib_gen))

        while True:
            next_num = nums[-1] + nums[-2]
            nums.pop(0)
            nums.append(next_num)
            yield next_num % prime_number

    def fib():
        Label(frame, text="что-то?").grid(row=5, column=0)
        xEntry = Entry(frame)
        xEntry.insert(0, '0')
        xEntry.grid(row=5, column=1)

        fib_rand(seed1Entry.get(), seed2Entry.get(), primeNumberEntry.get(), int(NEntry.get()))

    fibRandButton = Button(
        frame,
        text='fib_rand',
        command=fib)
    fibRandButton.grid(row=4, column=1)
