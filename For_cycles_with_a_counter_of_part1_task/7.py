# Задача 7. Пропавшая карточка
# Что нужно сделать
# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Напишите программу, которая поможет найти потерянную карточку,
# если номера оставшихся известны. Найдите её, зная номера оставшихся карточек.
#
# Введите число карточек — N.
#
# Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в любом порядке.

# if __name__ == '__main__':
#     N = int(input('Введите количество карточек: '))
#     fact = 1
#     summ_cards = 1
#     for cards in range(1, N):
#         number_cards = int(input('Введите номер оставшейся карточки: '))
#         summ_cards *= number_cards
#     for number in range(2, N+1):
#         fact *= number
#     print(fact//summ_cards)
#
if __name__ == '__main__':
    totalCards = int(input('Введите количество карточек: '))
    totalSumm = 0
    remainung_sum = 0
    for card in range(1, totalCards + 1):
        totalSumm += card
    for card in range(totalCards - 1):
        remainung_card = int(input('Введите номер оставшейся карты: '))
        totalSumm -= remainung_card
    print('Номер потерявшейся карточки: ', totalSumm)

