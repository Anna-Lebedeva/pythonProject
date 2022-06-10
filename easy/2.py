if __name__ == '__main__':
    sum_employee = int(input("Введите количество сотрудников: "))
    s = []
    for _ in range(sum_employee):
        s.append(int(input("Введите ID пропуска: ")))
    id_sotr = int(input("Какой id ищем? "))
    if id_sotr in s:input("Сотрудник работает!")
    else: input("Сотрудник не работает!")

