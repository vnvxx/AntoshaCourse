def myinputs() -> tuple[int, int, str]:
    while True:
        try:
            num1 = float(input("Введите число 1: "))
            num2 = float(input("Введите число 2: "))
            operator = input("Введите операцию которую вы хотите провести над числами: ")
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                break
            else:
                print("Вы ввели неверный знак операции!")
                return myinputs()
    return num1, num2, operator


def calc(num1: float, num2: float, operation: str) -> float:
    if operation == "+":
        num3 = num1 + num2
    elif operation == "-":
        num3 = num1 - num2
    elif operation == "*":
        num3 = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Деление на ноль нельзя!!!")
            return myinputs()
        else:
            num3 = num1 / num2
    return num3


def save(num3: float) -> None:
    save_decision = input("Результат вывести на экран или в тхт? Напишите 1 - Экран или 2 - Файл \n", )
    try:
        save_decision = int(save_decision)
    except ValueError:
        print("Выберите 1 или 2!!!")
    if save_decision == 1:
        print("Результат: ", num3)
    elif save_decision == 2:
        print("Запись выполнена!")
        with open("/output.txt", "w") as file:
            file.write(str(num3))
    else:
        print("Ошибка")
        return save(num3)


if __name__ == "__main__":
    num1, num2, operator = myinputs()
    results = calc(num1, num2, operator)
    save(results)