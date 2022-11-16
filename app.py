# Выполнил Прокофьев Андрей
# Фт-210008

import random

COMPARE_RESULT_WORD = {
    True: "больше",
    False: "меньше"
}


def get_int(text_to_print: str) -> int:
    while True:
        try:
            response = int(input(text_to_print + " >> "))

        except ValueError as value_error:
            print("Введите целое число! Ошибка:", value_error)

        else:
            return response


def main():
    """
    Главная функция
    """
    GUESS_VALUE_RANGE = get_int("Введите N")
    GUESS_ATTEMPTS_COUNT = get_int("Введите k")

    right_answer = random.randint(1, GUESS_VALUE_RANGE)

    while GUESS_ATTEMPTS_COUNT != 0:
        user_answer = get_int("Введите свой ответ")

        if user_answer == right_answer:
            break
        
        response = COMPARE_RESULT_WORD[user_answer > right_answer]
        print("Неправильно! Ваше число", response, "чем загаданное")
        GUESS_ATTEMPTS_COUNT -= 1

    # Проверка окончательного результата


if __name__ == "__main__":
    main()