# Линейный конгурэнтный метод
from functools import partial
from tkinter import *


def linear_congruential_method(a, c, m, x0, n):
    result = []
    xi = x0
    for i in range(n):
        xi = (a * xi + c) % m
        result.append(xi)

    # results = linear_congruential_method(1664525, 1013904223, 2 ** 32, 1, 10)

    # Взлом линейного конгурентного метода
    # a = 1664525
    # m = 2 ** 32
    # x0 = 1015568748
    # x1 = 1586005467
    # x2 = 2165703038


def restore_sequence(m, x0, x1, x2):
    for a in range(2, m):
        if a * (x1 - x0) % m == (x2 - x1) % m:
            break
        else:
            a = a + 1
    c = x2 - ((x1 * a) % m)
    return a, c

    Label(frame, text="a").grid(row=11, column=0)
    aEntry = Entry(frame)
    aEntry.insert(0, str(f(m, x0, x1, x2)))
    aEntry.grid(row=11, column=1)
