# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении, какую купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на двух вариантах:
#
# Взять квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть взять квартиру поменьше (от 80 м2), но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь и выводит сообщение о том, подходит она или нет.
#
if __name__ == '__main__':
    cost = int(input('Введите стоимость квартиры: '))
    s = int(input('Введите площадь квартиры: '))
    if cost <= 10 and s >= 100:
        print('Отличный выбор!')
    elif cost <= 7 and s >= 80:
        print('Отличный выбор!')
    else:
        print('Квартира не подходит:(')
