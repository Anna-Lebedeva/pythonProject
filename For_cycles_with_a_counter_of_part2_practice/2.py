# Задача 2. Деление клетки
# Реализуйте программу, разобранную в уроке.
#
# В одной лаборатории наблюдают за одноклеточной амёбой.
# Мы знаем, что каждые три часа она делится на 2 клетки.
# Нам нужно для этой лаборатории написать программу,
# которая будет выводить сколько прошло часов и сколько получилось клеток.
# Также нас попросили писать на каждом этапе деления сколько осталось часов до завершения наблюдения,
# чтобы ученым было проще формулировать выводы на определённом этапе наблюдения.
#
# Пример сообщений:
#
# Прошло часов: 3.
# Клеток: 2.
# Часов до конца эксперимента: 12
# Прошло часов: 6...

if __name__ == '__main__':
    cells = 1
    time = int(input('Введите количество часов: '))
    for hour in range(1, time // 3 + 1):
        cells *= 2

        print('Прошло часов: ', hour * 3)
        print('Количество клеток:', cells)
        print('Часов до конца эксперимента:', time - hour * 3 )
        print()
    print('Наблюдение завершено!')
