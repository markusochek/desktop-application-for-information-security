# Метод фибоначи с запаздыванием
def fib_rand_all(seed1, seed2, primeNumber, N):
    result = ""
    rand_gen = fib_rand(seed1, seed2, primeNumber, N)
    for i in range(10):
        result += str(next(rand_gen)) + "\n"
    return result


def fib_seq(seed1, seed2):
    """Генератор последовательности чисел Фибоначчи"""
    a, b = seed1, seed2
    while True:
        yield a
        a, b = b, a + b


def fib_rand(seed1, seed2, prime_number, n):
    """Генератор псевдослучайной последовательности по методу Фибоначчи"""
    fib_gen = fib_seq(seed1, seed2)
    nums = []
    for i in range(n):
        nums.append(next(fib_gen))
    while True:
        next_num = nums[-1] + nums[-2]
        nums.pop(0)
        nums.append(next_num)
        yield next_num % prime_number

# rand_gen = fib_rand(185, 19, 111, 10)
# for i in range(10):
#     print(next(rand_gen))