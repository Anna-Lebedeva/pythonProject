# Что нужно сделать
#
# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям.
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода. И так за каждый год.
# Надя решила, что быстрее будет написать простую программу, которая сделает всё за неё.
#
# Запросите у пользователя четыре числа.
# Отдельно сложите два первых и отдельно — два вторых.
# Разделите первую сумму на вторую.
# Выведите результат на экран.
if __name__ == '__main__':
    first_number = int(input('Введите сумму за первый квартал:'))
    second_number = int(input('Введите сумму за второй квартал:'))
    third_number = int(input('Введите сумму за третий квартал:'))
    fourth_number = int(input('Введите сумму за четвертый квартал:'))
    first_plus_second = first_number + second_number
    third_plus_fourth = third_number + fourth_number
    res = first_plus_second / third_plus_fourth
    print(res)