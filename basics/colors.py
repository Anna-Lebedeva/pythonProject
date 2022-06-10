# Исправьте программу так, чтобы в результате её выполнения на экран в одну строку
# выводился текст: Red Blue Green RedGreenBlue Blue GreenBlue.
#
# r = 'Red'
# g = 'Green'
# b = 'Blue'
#
# print(b, r, g, b, g + b, b + b + g, b)
if __name__ == '__main__':
    r = 'Red'
    g = 'Green'
    b = 'Blue'

    print(r, b, g, r + g + b, b, g+b)
