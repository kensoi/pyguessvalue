"""
Выполнил Прокофьев Андрей
Фт-210008
"""

import random


COMPARE_RESULT_WORD = {
    True: "больше",
    False: "меньше"
}


def get_int(text_to_print: str) -> int:
    """
    Получить целое число
    """

    while True:
        try:
            response = int(input(text_to_print + " >> "))
            # попытка не получить value error exception

            if response < 1:
                # если вдруг число меньше единицы, то
                # отправляем пользователя обратно писать число
                print("Число должно быть больше 0!")
                continue

        except ValueError as value_error:
            # если получили то отправляем пользователя обратно писать число
            print("Введите целое число! Ошибка:", value_error)
            continue

        return response


def main():
    """
    Главная функция
    """

    attempts_count = 1 # копия
    guess_value_range = get_int("Введите N") # const
    guess_attempts_count = get_int("Введите k") # const
    right_answer = random.randint(1, guess_value_range)

    while attempts_count <= guess_attempts_count:
        user_answer = get_int(f"Введите свой ответ [{attempts_count}/{guess_attempts_count}]")

        if user_answer == right_answer:
            break # если правильно, то остановить цикл.

        attempts_count += 1
        print("Неправильно! Ваше число",
            COMPARE_RESULT_WORD[user_answer > right_answer], # больше/меньше
            "чем загаданное.")

    # Проверка окончательного результата
    if user_answer == right_answer:
        print(f"Вы угадали с попытки №{attempts_count}!")

    else:
        print("Вы не угадали число и потратили все попытки! Загаданное число:", right_answer)


if __name__ == "__main__":
    main()
