# LFSR
import numpy as np
def lfsr_period():
    n = int(input('Введите длину регистра 4 или 8: '))
    ivr = []
    for i in range(n):
        iv = int(input('Введите значение ' + str(i+1) + ': '))
        ivr.append(iv)
    print(ivr, ivr[n - 1])
    x = ivr
    i = 0
    while True:
        i += 1
        e0 = 0
        if n == 8:
            e0 = (int(ivr[1]) + int(ivr[2]) + int(ivr[3]) + int(ivr[7])) % 2
        elif n == 4:
            e0 = (int(ivr[0]) + int(ivr[3])) % 2

        ivr = ivr[0:n - 1:]
        ivr.insert(0, e0)
        if ivr == x:
            print('Период равен ', i)
            break
        else:
            print(ivr, ivr[n - 1])
def solve_mod_2(A, B):
    x = np.linalg.solve(A, B)
    return x % 2

print(lfsr_period())