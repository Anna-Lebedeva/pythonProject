# Андрей любит играть в компьютерные игры.
# В один прекрасный день у него появилась классная идея для сюжета своей игры.
# Чтобы воплотить её в жизнь, он начал изучать программирование и геймдизайн.
# Начал он с главного героя и его системы прокачки.
#
# Напишите программу, которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.
#
if __name__ == '__main__':
    points = int(input('Введите количество очков: '))
    if points < 1000:
        print('Ваш уровень 1')
    elif points < 2500:
        print('Ваш уровень 2')
    else:
        print('Ваш уровень 3')