# Задача 5. Отрезок
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в консоль
# среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
if __name__ == '__main__':
    summa = 0
    count = 0
    result = 0
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    for number in range(a, b+1):
        if not number % 3:
            summa += number
            count += 1
    if count != 0:
        result = summa / count
    print(result)
