"""
Выполнил Прокофьев А.А.
Фт-210008
"""

import logging
from enum import Enum # для упрощения вида

class LogLevel(Enum):
    """
    Уровни логгирования.
    """

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

LOGGER_FILE_NAME = ".log" # название файла, куда должен записываться лог
LOGGER_LEVEL = LogLevel.INFO # = 50
LOGGER_FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s') # форма записи в файл

logger = logging.getLogger("Логгер угадайки") # получаем сам логгер
logger.setLevel(LOGGER_LEVEL.value) # устанавливаем уровень записи

file_handler = logging.FileHandler(LOGGER_FILE_NAME, 'a', 'utf-8') # создаём обработчик файла
file_handler.setLevel(LOGGER_LEVEL.value) # устанавливаем уровень записи
file_handler.setFormatter(LOGGER_FORMATTER) # устанавливаем форму записи в файле
logger.addHandler(file_handler) # добавляем обработчик в логгер

# logger.log(LogLevel.DEBUG.value, "hello world") # логгирование на уровне DEBUG = 10
# первый аргумент - см. значения logger_level

def log_message(log_level: LogLevel, message: str):
    """
    Обёртка вокруг logger.log
    """

    logger.log(log_level.value, message)
