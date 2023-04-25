# Линейный конгурэнтный метод
from functools import partial
from tkinter import *


def linear_congruential_method(a, c, m, x0, n):
    result = ""
    xi = x0
    for i in range(n):
        xi = (a * xi + c) % m
        result += str(xi) + "\n"
    return result

    # results = linear_congruential_method(1664525, 1013904223, 1, 10)

    # Взлом линейного конгурентного метода
    # a = 1664525
    # x0 = 1015568748
    # x1 = 1586005467
    # x2 = 2165703038


def restore_sequence(m, x0, x1, x2):
    a = 0
    for a in range(2, m):
        if a * (x1 - x0) % m == (x2 - x1) % m:
            break
        else:
            a = a + 1
    c = x2 - ((x1 * a) % m)
    return [a, c]
