"""
Выполнил Прокофьев Андрей
Фт-210008
"""

import random
from logger import LogLevel, log_message


COMPARE_RESULT_WORD = {
    True: "больше",
    False: "меньше"
}


def get_int(text_to_print: str) -> int:
    """
    Получить целое число
    """

    while True:
        log_message(LogLevel.DEBUG, "Попытка взять целое число")
        try:
            response = int(input(text_to_print + " >> "))
            # попытка не получить value error exception
            log_message(LogLevel.DEBUG, "Число взято")

            if response < 1:
                # если вдруг число меньше единицы, то
                # отправляем пользователя обратно писать число
                log_message(LogLevel.DEBUG, "Число взято меньше нуля")
                print("Число должно быть больше 0!")
                continue

        except ValueError as value_error:
            # если получили то отправляем пользователя обратно писать число
            log_message(LogLevel.DEBUG, "Пользователь ввёл неверное число")
            print("Введите целое число! Ошибка:", value_error)
            continue

        log_message(LogLevel.DEBUG, "Число взято согласно условиям")
        return response


def main():
    """
    Главная функция
    """
    log_message(LogLevel.INFO, "Программа запущена")

    attempts_count = 1 # копия
    guess_value_range = get_int("Введите N") # const
    attempts_total_count = get_int("Введите k") # const
    right_answer = random.randint(1, guess_value_range)

    log_message(LogLevel.INFO, "Начало угадайки")
    log_message(LogLevel.INFO, f"Загаданное число: {right_answer}")
    log_message(LogLevel.INFO, f"Количество попыток: {attempts_total_count}")

    while attempts_count <= attempts_total_count:
        log_message(LogLevel.INFO, f"Попытка №{attempts_count}")
        user_answer = get_int(f"Введите свой ответ [{attempts_count}/{attempts_total_count}]")

        if user_answer == right_answer:
            print()
            log_message(LogLevel.INFO, "Попытка успешна!")
            break # если правильно, то остановить цикл.

        attempts_count += 1
        log_message(LogLevel.INFO, "Попытка неудачна!")
        print("Неправильно! Ваше число",
            COMPARE_RESULT_WORD[user_answer > right_answer], # больше/меньше
            "чем загаданное.")
        print()

    # Проверка окончательного результата
    log_message(LogLevel.INFO, "Проверка результатов")
    if user_answer == right_answer:
        log_message(LogLevel.INFO, "Игрок выиграл")
        print(f"Вы угадали с попытки №{attempts_count}!")

    else:
        log_message(LogLevel.INFO, "Компьютер выиграл")
        print("Вы не угадали число и потратили все попытки! Загаданное число:", right_answer)

    log_message(LogLevel.INFO, "Конец игры")


if __name__ == "__main__":
    main()
