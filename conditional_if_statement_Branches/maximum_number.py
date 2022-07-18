# Пользователь вводит три числа.
#
# Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Используйте дополнительные переменные, если нужно.
#
# if __name__ == '__main__':
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     num3 = int(input('Введите третье число: '))
#     if num1 > num2 and num1 > num2:
#         print('Большее число', num1)
#     if num2 > num1 and num2 > num3:
#         print('Большее число', num2)
#     if num3 > num1 and num3 > num2:
#         print('Большее число', num3)
if __name__ == '__main__':
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    num3 = int(input('Введите третье число: '))
    max1 = 0
    max2 = 0
    max3 = 0

    if num1 > num2:
        max1 = 1
    if num1 > num3:
        max1 = max1 + 1
    if max1 == 2:
        print('Большее число', num1)

    if num2 > num1:
        max2 = 1
    if num2 > num3:
        max2 = max2 + 1
    if max2 == 2:
        print('Большее число', num2)

    if num3 > num1:
        max3 = 1
    if num3 > num2:
        max3 = max3 + 1
    if max3 == 2:
        print('Большее число', num3)

    # num1 = int(input('Введите первое число: '))
    # num2 = int(input('Введите второе число: '))
    # num3 = int(input('Введите третье число: '))
    #
    # max_num = num1
    # if num2 > max_num:
    #     max_num = num2
    # if num3 > max_num:
    #     max_num = num3
    # print('Большее число', max_num)
