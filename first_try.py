'''12 вариант. 1 функция'''

def factorial(n):
    """Функция для вычисления факториала числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def calculate_exponential(x, n=5):
    """Функция для вычисления e^x по формуле ряда Тейлора."""
    e_x = 0
    for i in range(n + 1):
        e_x += (x ** i) / factorial(i)
    return e_x

'''12 вариант. 2 функция'''

def factorial(n):
    """Вычисляет факториал числа n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_hyperbolic_cosine(x, n=5):
    """Вычисляет гиперболический косинус ch(x) с использованием ряда Тейлора."""
    ch_x = 0
    for i in range(n + 1):
        ch_x += (x ** (2 * i)) / factorial(2 * i)
    return ch_x


def main():
    while True:
        print('     МЕНЮ     ')
        print('1. Ряд Маклорена для экспоненты')
        print('2. Ряд Маклорена для гиперболического косинуса.')
        print('3. Выход')
        
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                x = float(input("Введите значение x: "))
                result = calculate_exponential(x)
                print(f"Приближенное значение e^{x} = {result}")
            except ValueError:
                print('Ошибка. Введите числа.')
        elif choice == '2':
            try:
                x = float(input("Введите значение x: "))
                result = calculate_hyperbolic_cosine(x)
                print(f"Приближенное значение ch({x}) = {result}")
            except ValueError:
                print('Ошибка. Введите числа.')
        elif choice == '3':
            print('Выход из программы')
            break
        else:
            print('Ошибка. Выберите правильный пункт меню.')

if __name__ == '__main__':
    main()