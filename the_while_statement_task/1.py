# Задача 1. Кубы чисел
#
# Что нужно сделать
#
# У любителя математики Паши есть распечатанные таблички со степенями двойки.
# Теперь он хочет взять степень тройки от единицы до абсолютно любого числа!
#
# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.
if __name__ == '__main__':
    number = int(input('Введите до какого числа нужно возвести в третью степень: '))
    count = 1
    while number >= count:
        result = count ** 3
        print(count, '** 3 =', result)
        count += 1