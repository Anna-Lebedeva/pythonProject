# Задача 6. Замечательные числа
# Что нужно сделать
# Напишите программу, которая находит и выводит все двузначные числа,
# равные утроенному произведению своих цифр. К таким относятся, например, 15 и 24.
#
if __name__ == '__main__':
    for number in range(10, 100):
        first_digit = number % 10
        second_digit = number // 10
        if number == 3 * first_digit * second_digit:
            print(number)