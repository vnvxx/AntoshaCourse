def main_block():
    print('Введите два числа для вычислений:')
    while True:
        try:
            num1 = float(input('Введите первое число:'))
            num2 = float(input('Введите второе число:'))
            break
        except ValueError:
            print('Ошибка!!! Повторите ввод чисел')

    print('Выберите операцию над числами:\n'
          '1. Сложение.\n'
          '2. Вычитание.\n'
          '3. Умножение.\n'
          '4. Деление.')
    choice = input('Выберите операцию над числом, введя 1, 2, 3 или 4!: ')
    if choice == '1':
        num3 = num1+num2
        print(f"Сумма двух чисел равно {num3}")
    elif choice == '2':
        num3 = num1-num2
        print(f"Вычитание двух числе равно {num3}")
    elif choice == '3':
        num3 = num1*num2
        print(f"Умножение двух числе равно {num3}")
    elif choice == '4':
        if num2 == 0:
            print("Деление невозможно!!!")
        else:
            num3 = num1 / num2
            print(f"Деление двух числе равно {num3}")


if __name__ == "__main__":
    main_block()