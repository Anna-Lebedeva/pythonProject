# Вы уже писали программу, вычисляющую сумму налога по прогрессивной шкале
# в зависимости от полученного заработка: 13% на доход до 10 000,
# 20% на доход от 10 000 до 50 000, 30% на доход выше 50 000.
#
# Однако во многих странах, использующих такую шкалу,
# эта сумма вычисляется более сложным способом: налоговая ставка 30% на доход выше 50 000 означает,
# что 30% уплачивается не со всей суммы, а лишь с той её части, которая превосходит 50 000.
# Аналогично ставка 20% на доход от 10 000 до 50 000 обязывает уплатить 20% лишь с той части суммы,
# которая превосходит 10 000, но не превосходит 50 000.
#
# Так, например, с дохода 100 000 придётся заплатить такой налог:
# 30% × (100 000 − 50 000) + 20% × (50 000 − 10 000) + 13% × 10 000 = 15 000 + 8 000 + 1 300 = 24 300
# А с дохода 30 000 — такой:  20% × (30 000 − 10 000) + 13% × 10 000 = 4 000 + 1 300 = 5 300
# Напишите программу, которая спрашивает у пользователя его доход и
# высчитывает сумму налога для него по вышеописанным правилам.
if __name__ == '__main__':
    salary = int(input('Введите зарплату: '))
    if salary > 50000:
        nalog = (salary - 50000) * 0.3 + 9300
        print(nalog)
    elif salary < 10000:
        nalog = salary * 0.13
        print(nalog)
    else:
        nalog = (salary - 10000) * 0.2 + 1300
        print(nalog)