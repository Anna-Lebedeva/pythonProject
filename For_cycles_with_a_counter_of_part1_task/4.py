# Задача 4. Успеваемость в классе
# Что нужно сделать
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
# Напишите программу, которая получает список оценок — N чисел — и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.
#
# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

if __name__ == '__main__':
    troechnik = 0
    good_guy = 0
    excellent_student = 0
    count = int(input('Сколько в классе человек? '))
    for people in range(1, count+1):
        people = int(input(f"Введите оценку {people} ученика: "))
        if people == 3:
            troechnik += 1
        elif people == 4:
            good_guy += 1
        elif people == 5:
            excellent_student += 1
    if troechnik > good_guy and troechnik > excellent_student:
        print('Троечников больше всего!')
    elif good_guy > troechnik and good_guy > excellent_student:
        print('Хорошистов больше всего!')
    else:
        print('Отличников больше всего!')

        # Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.!!!