# Костя играет в азартную игру с кубиками с владельцем заведения.
# Правда, с довольно интересными правилами: если у Кости на кубике выпадет столько же или больше,
# чем у владельца, то Костя задолжает разность в тысячах долларов.
# Однако если выпадет меньше, то Косте выплатят столько тысяч долларов, сколько будет сумма очков на кубиках.
#
# Напишите программу. На вход в программу подаётся два числа.
# Если первое число больше либо равно второму, нужно вывести на экран их разность
# и отдельной строкой фразу: «Костя платит». В противном случае вывести их сумму
# и отдельной строкой — фразу: «Владелец платит». Также последней строкой в результате
# нужно вывести на экран фразу: «Игра окончена».

if __name__ == '__main__':
    kostya = int(input('Введите значение, которое выпало Косте: '))
    owner = int(input('Введите значение, которое выпало владельцу: '))
    if kostya >= owner:
        print(kostya-owner, 'Костя платит')
    else:
        print(kostya+owner, 'Владелец платит')
print('Игра окончена')
