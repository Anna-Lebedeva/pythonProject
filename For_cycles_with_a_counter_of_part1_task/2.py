# Задача 2. Посчитай чужую зарплату...
# Что нужно сделать
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и,
# чтобы облегчить себе жизнь, обратилась к программисту.
#
# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

if __name__ == '__main__':
    salary = 0
    for money in range(1, 13):
        money = int(input(f"Введите зарплату за {money} месяц: "))
        salary += money
    salary = salary / 12
    print('Ваша средняя зарплата за год:', salary)