# Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:

# Первое и последнее числа последовательности должны поменяться местами.
# В конец списка нужно добавить сумму всех чисел.


# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
L = list(map(float, input("Введите значение: ").split()))

# обмениваем первое и последнее число
# с помощью множественного присваивания
L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем её в конец списка
L.append(sum(L))

print(L)