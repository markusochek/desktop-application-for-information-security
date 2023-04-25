# Генератор последовательности от движения мышки
import ctypes
import time


def get_mouse_symbol():
    symbol = ''
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

    for i in range(20):
        point = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.pointer(point))
        time.sleep(0.2)
        symbol += chr((point.x % 90 ** point.y % 90) % 90 + 33)

    return symbol
