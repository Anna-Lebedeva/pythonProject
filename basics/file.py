# Напишите программу, которая запрашивает у пользователя его имя
# и имя файла (переменные user и new_file соответственно).
# Используя операцию конкатенации, выведите путь к файлу на экран.

if __name__ == '__main__':
    user = input('Введите пользователя: ')
    new_file = input('Введите имя файла: ')
    print("Путь к файлу: C:/" + user + "/docs/folder/" + new_file + ".txt")
