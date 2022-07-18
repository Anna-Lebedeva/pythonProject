# В некоторых странах действует так называемая прогрессивная шкала налогообложения:
# чем больше ты зарабатываешь, тем больший налог платишь.
# Нужно написать программу, которая будет рассчитывать сумму налога исходя из прибыли.
# Если прибыль до 10 000 — ставка налога равна 13%, начиная с 10 000 и до 50 000 — 20%.
# А начиная с 50 000 — 30%. А также нужно добавить «проверку на дурака»: если ввели число меньше нуля,
# то вывести сообщение: «Ошибка: доход не может быть отрицательным».

if __name__ == '__main__':
    salary = int(input('Введите зарплату: '))
    if salary < 0:
        print('Ошибка: доход не может быть отрицательным')
    elif salary < 10000:
        nalog = salary * 0.13
        print('Налог равен:', nalog)
    elif salary <= 50000:
        nalog = salary * 0.2
        print('Налог равен:', nalog)
    else:
        nalog = salary * 0.3
        print('Налог равен:', nalog)