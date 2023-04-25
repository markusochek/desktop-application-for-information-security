from tkinter import *

from Program3 import linear_congruential_method, restore_sequence
def formsProgram3(window, frame):
        m = 3 ** 32

        # Label(frame, text="result").grid(row=6, column=0)
        # resultEntry = Entry(frame)
        # resultEntry.insert(0, str(result))
        # resultEntry.grid(row=6, column=1)
        #
        # Label(frame, text="x0").grid(row=7, column=0)
        # x0Entry = Entry(frame)
        # x0Entry.insert(0, '0')
        # x0Entry.grid(row=7, column=1)
        #
        # Label(frame, text="x1").grid(row=8, column=0)
        # x1Entry = Entry(frame)
        # x1Entry.insert(0, '0')
        # x1Entry.grid(row=8, column=1)
        #
        # Label(frame, text="x2").grid(row=9, column=0)
        # x2Entry = Entry(frame)
        # x2Entry.insert(0, '0')
        # x2Entry.grid(row=9, column=1)
        #
        # restoreSequenceButton = Button(
        #     frame,
        #     text='restore_sequence',
        #     command=partial(restore_sequence,
        #                     m,
        #                     x0Entry.get(),
        #                     x1Entry.get(),
        #                     x2Entry.get()))
        # restoreSequenceButton.grid(row=10, column=1)
        #
        # names = ["введите a",
        #          "введите c",
        #          "введите x0",
        #          "введите n"]
        # entries = []
        #
        # for i in range(4):
        #     Label(frame, text=names[i]).grid(row=i, column=0)
        #
        #     entries.append(Entry(frame))
        #     entries[i].insert(0, '0')
        #     entries[i].grid(row=i, column=1)
        #
        # linearButton = Button(
        #     frame,
        #     text='linear',
        #     command=partial(linear_congruential_method,
        #                     entries[0].get(),
        #                     entries[1].get(),
        #                     entries[2].get(),
        #                     entries[3].get(),
        #                     int(entries[4].get()))
        # )
        # linearButton.grid(row=5, column=1)