'''12 вариант. 1 функция'''

def factorial(n):
    """Функция для вычисления факториала числа n.
    
    Подробное описание:
    Эта функция вычисляет факториал заданного неотрицательного 
    целого числа n, используя итеративный подход.

    Аргументы:
        n (int): Неотрицательное целое число, для которого нужно вычислить факториал.

    Возвращаемое значение:
        int: Факториал числа n (n!).

    Исключения:
        ValueError: Генерируется, если n является отрицательным числом.

    Примеры использования:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def calculate_exponential(x, n=5):
    """Функция для вычисления e^x по формуле ряда Тейлора.
    
    Подробное описание:
    Эта функция вычисляет приближенное значение e^x с помощью 
    ряда Тейлора. Количество членов ряда определяется параметром n.
    
    Аргументы:
        x (float): Значение, для которого необходимо вычислить e^x.
        n (int, optional): Количество членов ряда, которые будут 
            использованы для приближенных вычислений. По умолчанию 5.

    Возвращаемое значение:
        float: Приближенное значение e^x.

    Исключения:
        None.

    Примеры использования:
        >>> calculate_exponential(1)
        2.71828...
        >>> calculate_exponential(0, n=10)
        1.0
    """
    e_x = 0
    for i in range(n + 1):
        e_x += (x ** i) / factorial(i)
    return e_x

'''12 вариант. 2 функция'''

def factorial(n):
    """Вычисляет факториал числа n.

    Подробное описание:
    Эта функция вычисляет факториал заданного неотрицательного 
    целого числа n. Факториал числа n (обозначаемый n!) это произведение всех 
    положительных целых чисел от 1 до n. Например, 5! = 5 × 4 × 3 × 2 × 1 = 120.

    Аргументы:
        n (int): Неотрицательное целое число, для которого требуется 
                  вычислить факториал.

    Возвращаемое значение:
        int: Факториал числа n (n!).

    Исключения:
        ValueError: Генерируется, если n является отрицательным числом.

    Примеры использования:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_hyperbolic_cosine(x, n=5):
    """Вычисляет гиперболический косинус ch(x) с использованием ряда Тейлора.

    Подробное описание:
    Эта функция вычисляет приближенное значение гиперболического косинуса 
    \( \text{ch}(x) \) с помощью разложения в ряд Тейлора. 
    Формально, гиперболический косинус определяется как:
    
\[
    \text{ch}(x) = \sum_{i=0}^{\infty} \frac{x^{2i}}{(2i)!}
    \]
    Для численного вычисления используется конечное число членов \( n \) 
    в ряде Тейлора.

    Аргументы:
        x (float): Значение, для которого необходимо вычислить гиперболический косинус.
        n (int, optional): Количество членов ряда для использования (по умолчанию 5).

    Возвращаемое значение:
        float: Приближенное значение гиперболического косинуса ch(x).

    Исключения:
        Нет.

    Примеры использования:
        >>> calculate_hyperbolic_cosine(0)
        1.0
        >>> calculate_hyperbolic_cosine(1)
        1.5430806348152437
        >>> calculate_hyperbolic_cosine(2, n=10)
        3.7621956910836314
    """
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