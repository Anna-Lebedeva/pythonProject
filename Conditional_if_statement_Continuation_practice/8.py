# Илья хочет в лучший вуз страны, а для этого нужно не только хорошо сдать экзамены
# (балл должен быть больше 280), но и иметь золотую медаль.
#
# Напишите программу, которая запрашивает у пользователя два числа:
# результат экзаменов и наличие золотой медали (0 — нет медали, 1 — медаль есть),
# а затем проверяет, поступил ли Илья в вуз. Выведите соответствующее сообщение.
#
if __name__ == '__main__':
    rez_exam = int(input('Введите количество баллов, полкченные за экзамены: '))
    medal = int(input('Введите наличие медали, 0 — нет медали, 1 — медаль есть '))
    if rez_exam > 280 and medal == 1:
        print('Вы поступили!')
    else:
        print('Вы не поступили.')
