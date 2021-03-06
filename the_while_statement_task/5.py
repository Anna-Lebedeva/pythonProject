# Задача 5. Счастливый билетик
#
# Что нужно сделать
#
# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье: если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх, то это к удаче.
#
# Напишите программу, которая получала бы на входе шестизначный номер билета и выводила,
# счастливый это билет или нет. К примеру, билеты 666 666 и 252 135 — счастливые, а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?
#
if __name__ == '__main__':
    ticket = int(input('Введите шестизначный номер билета: '))
    num6 = ticket % 10
    print(num6)
    num5 = (ticket // 10) % 10
    print(num5)
    num4 = (ticket // 100) % 10
    print(num4)
    num3 = (ticket // 1000) % 10
    print(num3)
    num2 = (ticket // 10000) % 10
    print(num2)
    num1 = (ticket // 100000) % 10
    print(num1)
    if num6 + num5 + num4 == num3 + num2 + num1:
        print('Билет счастливый!')
    else:
        print('Билет несчастливый!')