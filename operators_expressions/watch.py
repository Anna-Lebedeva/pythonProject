# Напишите программу, которая получает на вход число n (количество минут),
# затем считает, сколько это будет в часах и сколько минут останется, и выводит на экран эти два результата.
if __name__ == '__main__':
    amount = int(input('Введите количество минут: '))
    hour = amount // 60
    print('В часах это:', hour, 'часа(ов)')
    print('и останется минут до полного часа:', amount - hour * 60)