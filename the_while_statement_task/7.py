# Задача 7. Обычный день на работе
#
# Что нужно сделать
#
# Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
#
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
#
if __name__ == '__main__':
    count = 8
    summ_task = 0
    while count > 0:
        task = int(input('Введите количество новых задач: '))
        summ_task += task
        phone = int(input('Звонит жена. Взять трубку? 1/0: '))
        count -= 1
    print(summ_task)
    if phone == 1:
        print('Нужно зайти в магазин')

