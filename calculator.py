'''
Программа-калькулятор с базовыми математическими операциями
Поддерживает: сложение, вычитание, умножение, деление, возведение в степень, извлечение корня
'''

import math

def show_menu():
    print("\n" + "="*50)
    print("      КАЛЬКУЛЯТОР")
    print("="*50)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Выход")
    print("="*50)

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")


def addition(a, b):
    """Сложение двух чисел."""
    return a + b

def subtraction(a, b):
    """Вычитание второго числа из первого."""
    return a - b

def multiplication(a, b):
    """Умножение двух чисел."""
    return a * b

def division(a, b):
    """Деление первого числа на второе. Вызывает ZeroDivisionError при делении на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b

def exponentiation(base, exponent):
    """Возведение base в степень exponent."""
    return base ** exponent

def square_root(number):
    """Извлечение квадратного корня. Вызывает ValueError при отрицательном аргументе."""
    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определён.")
    return math.sqrt(number)


def addition_ui():
    print("\n--- СЛОЖЕНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = addition(num1, num2)
    print(f"Результат: {num1} + {num2} = {result}")

def subtraction_ui():
    print("\n--- ВЫЧИТАНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = subtraction(num1, num2)
    print(f"Результат: {num1} - {num2} = {result}")

def multiplication_ui():
    print("\n--- УМНОЖЕНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = multiplication(num1, num2)
    print(f"Результат: {num1} × {num2} = {result}")

def division_ui():
    print("\n--- ДЕЛЕНИЕ ---")
    num1 = get_number("Введите делимое: ")
    while True:
        num2 = get_number("Введите делитель: ")
        try:
            result = division(num1, num2)
            break
        except ZeroDivisionError as e:
            print(f"Ошибка! {e}")
    print(f"Результат: {num1} ÷ {num2} = {result}")

def exponentiation_ui():
    print("\n--- ВОЗВЕДЕНИЕ В СТЕПЕНЬ ---")
    base = get_number("Введите основание: ")
    exponent = get_number("Введите степень: ")
    result = exponentiation(base, exponent)
    print(f"Результат: {base} ^ {exponent} = {result}")

def square_root_ui():
    print("\n--- КВАДРАТНЫЙ КОРЕНЬ ---")
    while True:
        number = get_number("Введите число: ")
        try:
            result = square_root(number)
            break
        except ValueError as e:
            print(f"Ошибка! {e}")
            print("Пожалуйста, введите неотрицательное число.")
    print(f"Результат: √{number} = {result}")


def main():
    print("Добро пожаловать в калькулятор!")
    while True:
        show_menu()
        choice = input("Выберите операцию (1-7): ")

        if choice == '1':
            addition_ui()
        elif choice == '2':
            subtraction_ui()
        elif choice == '3':
            multiplication_ui()
        elif choice == '4':
            division_ui()
        elif choice == '5':
            exponentiation_ui()
        elif choice == '6':
            square_root_ui()
        elif choice == '7':
            print("Спасибо за использование калькулятора! До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите операцию от 1 до 7.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()