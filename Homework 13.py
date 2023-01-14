cost = 0

try:
    N = int(input('Введите количество билетов: '))
    if N <= 0:
        raise ValueError("Значение должно быть больше 0!")
except ValueError as error:
    print(error)
    print("Неверное значение")
else:
    for i in range(1, N+1):
        age = int(input(f'Введите возраст участника для билета №{i}: '))
        if age < 18:
            cost += cost
        elif (18 >=age< 25):
            cost += 990
        else:
            cost += 1390
        print('Стоимость билета для участника:', cost, 'руб.')
    print('Предварительная сумма покупки равна:', cost, 'руб.')

    if N >= 3:
        cost -= 0.1*cost

print('Итоговая сумма покупки равна:', cost, 'руб.')
