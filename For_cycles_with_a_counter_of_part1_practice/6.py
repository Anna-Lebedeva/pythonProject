# Задача 3. Любовь с первой цифры (цикл for)
# Перепишите программу из прошлого модуля, используя цикл for.
# Паша очень любит математику. Настолько сильно, что у него по всей комнате висят всякие таблицы умножения,
# сложения, какие-то графики, формулы. И теперь он захотел распечатать таблицу степеней двойки,
# у них как раз началась новая тема по информатике.
# Используя цикл for, выведите на экран для числа 2 его степени от 0 до 20.

if __name__ == '__main__':
    for number in range(21):
        print(number ** 2)
