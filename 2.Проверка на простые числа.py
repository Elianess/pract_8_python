"""
Код приведенный ниже,найдет простое число из списка чисел,
а также сгенерирует первые 10 простых чисел.
"""
from kanren import isvar, run, membero
from kanren.core import success, fail, goaleval, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime
import itertools as it

#определим функцию, которая будет проверять простые числа
def prime_check(x):
    if isvar(x):
        return(condeseq([(eq, x, p)] for p in map(prime, it.count(1))))
    else:
        return(success if isprime(x) else fail)

#определяем переменную
x = var('x')

#результат
print((set (run (0, x, (membero, x, (12, 14, 15, 19, 20, 21, 22, 23, 29, 30, 41, 44, 52, 62, 65, 85)), (prime_check, x)))))
print((run (10, x, prime_check(x))))