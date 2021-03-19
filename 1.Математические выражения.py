from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

#определяем математические операции, которые мы собираемся использовать
add = 'add'#сложение
mul = 'mul'#умножение

#и сложение, и умножение являются коммуникативными процессами, указываем это
fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

#определяем переменные
a, b = var('a'), var('b')

"""
нужно сопоставить выражение с исходным шаблоном. есть следующий
оригинальный шаблон (5 + a) * b
"""
Original_pattern = (mul, (add, 5, a), b)

"""
есть два выражения, которые соответствуют исходному шаблону - 3, 4
"""
exp1 = (mul, 2, (add, 3, 1))
exp2 = (add, 5, (mul, 8, 1))
exp3 = (mul, (add, 5, a), b)
exp4 = (mul, (add, 5, a), 2)

#вывод
print(run(0, (a,b), eq(Original_pattern, exp1)))#eq - конструктор цели указывает, что два выражения равны
print(run(0, (a,b), eq(Original_pattern, exp2))) 
print(run(0, (a,b), eq(Original_pattern, exp3)))
print(run(0, (a,b), eq(Original_pattern, exp4)))