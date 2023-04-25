# LFSR
from functools import partial
from tkinter import *


def program2(window, frame):
    polynomialLabel = Label(frame, text="введите polynomial")
    polynomialLabel.grid(row=0, column=0)
    polynomialEntry = Entry(frame)
    polynomialEntry.grid(row=0, column=1)

    # seedLabel = Label(frame, text="введите seed")
    # seedLabel.grid(row=1, column=0)
    # seedEntry = Entry(frame)
    # seedEntry.grid(row=1, column=1)

    def lfsr():
        seed = 0x1F
        sequence = lfsr_sequence(polynomialEntry.get(), seed)

        sequenceEntry = Entry(frame)
        sequenceEntry.insert(0, str(sequence))
        sequenceEntry.grid(row=3, column=1)

        newSequenceLabel = Label(frame, text="введите выделенный массив")
        newSequenceLabel.grid(row=4, column=0)
        newSequenceEntry = Entry(frame)
        newSequenceEntry.grid(row=4, column=1)
        newSequenceEntry.insert(0, str(sequence))

        lfsrRestoreButton = Button(
            frame,
            text='lfsr_restore',
            command=partial(lfsr_restore, newSequenceEntry.get())
        )
        lfsrRestoreButton.grid(row=5, column=1)

    def lfsr_sequence(polynomial, seed):
        sequence = []
        register = seed

        while True:
            bit = register >> (len(polynomial) - 1) & 1
            new_bit = bit ^ sum([int(polynomial[i]) * ((register >> i) & 1) for i in range(len(polynomial) - 1)])
            register = ((register << 1) & (2 ** len(polynomial) - 1)) | new_bit
            sequence.append(bit)
            if register == seed:
                break

        return sequence

    lfsrSequenceButton = Button(
        frame,
        text='lfsr_sequence',
        command=lfsr
    )
    lfsrSequenceButton.grid(row=2, column=1)

    def lfsr_restore(sequence):
        newStr = sequence[1:len(sequence)-1]
        newStr = newStr.split(", ")
        sequence = list[int](newStr)
        for i in range(len(sequence)):
            sequence[i] = int(sequence[i])

        l = 0
        state = [0] * len(sequence)
        c = [0] * len(sequence)
        c[0] = 1

        for i in range(len(sequence)):
            feedback = 0
            for j in range(l + 1):
                feedback ^= c[j] * sequence[i - j]

            if feedback == 1:
                temp = c.copy()
                d = i - l
                for j in range(len(c) - d):
                    c[d + j] ^= state[j]
                l = i + 1 - l
                state = temp

        polynomial = ''
        for i in range(l):
            polynomial += str(c[i])

        seed = int(''.join([str(bit) for bit in state[0:l][::-1]]), 2)

        restoredSequenceEntry = Entry(frame)
        restoredSequenceEntry.insert(0, str(lfsr_sequence(polynomial, seed)))
        restoredSequenceEntry.grid(row=6, column=1)
