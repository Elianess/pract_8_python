"""
There are five houses.
The English man lives in the red house.
The Swede has a dog.
The Dane drinks tea.
The green house is immediately to the left of the white house.
They drink coffee in the green house.
The man who smokes Pall Mall has birds.
In the yellow house they smoke Dunhill.
In the middle house they drink milk.
The Norwegian lives in the first house.
The man who smokes Blend lives in the house next to the house with cats.
In a house next to the house where they have a horse, they smoke Dunhill.
The man who smokes Blue Master drinks beer.
The German smokes Prince.
The Norwegian lives next to the blue house.
They drink water in a house next to the house where they smoke Blend.
"""
from kanren import *
from kanren.core import lall
import time

#определяем две функции left () и next (), чтобы проверить, чей дом оставлен или рядом с чьим-то домом
def left(q, p, list):
    return membero((p, q),  zip(list, list[1:]))#membero (item, coll) - утверждает, что item является членом коллекции coll.
def next(q, p, list):
    return conde([left(q, p, list)], [left(p, q, list)])#conde - конструктор целей для логических "и" и "или".

#объявим переменную house
houses = var()

#определяем правила с помощью пакета lall,
rules_zebraproblem = lall(
    #5 домов
    (eq, (var(), var(), var(), var(), var()), houses),
    #англичанин в красном доме
    (membero,('Englishman', var(), var(), var(), 'red'), houses),
    #у свида есть собака
    (membero,('Swede', var(), var(), 'dog', var()), houses),
    #дани пьет чай
    (membero,('Dane', var(), 'tea', var(), var()), houses),
    #зеленый дом слева от белого
    (left,(var(), var(), var(), var(), 'green'), (var(), var(), var(), var(), 'white'), houses),
    #кофе пьют в зеленом доме
    (membero,(var(), var(), 'coffee', var(), 'green'), houses),
    #у чела, который курит пол-мол есть птицы
    (membero,(var(), 'Pall Mall', var(), 'birds', var()), houses),
    #в желтом доме - чел курящий данхил
    (membero,(var(), 'Dunhill', var(), var(), 'yellow'), houses),
    #в доме посередине - пьют молоко
    (eq,(var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
    #норвежец в первом доме
    (eq,(('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
    #чел курящий бленд - рядом с домом где есть кошки 
    (next,(var(), 'Blend', var(), var(), var()), (var(), var(), var(), 'cats', var()), houses),
    #чел курящий донхел - рядом с домом где есть лошадь
    (next,(var(), 'Dunhill', var(), var(), var()), (var(), var(), var(), 'horse', var()), houses),
    #чел курящий блу мастер - пьет пиво
    (membero,(var(), 'Blue Master', 'beer', var(), var()), houses),
    #немец - курит принц
    (membero,('German', 'Prince', var(), var(), var()), houses),
    #норвежец - рядом с голубым домом
    (next,('Norwegian', var(), var(), var(), var()), (var(), var(), var(), var(), 'blue'), houses),
    #в доме рядом с челом крящим бленд - пьют воду
    (next,(var(), 'Blend', var(), var(), var()), (var(), var(), 'water', var(), var()), houses),
    #в одном из домом есть зебра
    (membero,(var(), var(), var(), 'zebra', var()), houses)
 )

#запускаем решатель с предыдущими ограничениями
solutions = run(0, houses, rules_zebraproblem)

#извлекаем вывод из решателя
output_zebra = [house for house in solutions[0] if 'zebra' in house][0][0]

#печатаем решение 
print ('\n'+ output_zebra + ' owns zebra.')
