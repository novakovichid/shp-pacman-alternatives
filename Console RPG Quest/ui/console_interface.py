"""Консольный интерфейс консольной RPG."""

from settings import Settings


class ConsoleInterface:
    """Отвечает за вывод текстовых сообщений."""

    def __init__(self, service):
        self.service = service

    def show_greeting(self):
        """Печатает приветствие и краткое описание игры."""
        print(f"Добро пожаловать в {Settings.APP_NAME}!")
        print("Эта версия содержит только структуру проекта.")

    def show_placeholder(self):
        """Выводит подсказку о дальнейших шагах."""
        print("Изучите каталог tasks/, чтобы увидеть план разработки.")

    def prompt_player_name(self):
        """Запрашивает имя игрока у пользователя."""
        pass

    def display_summary(self):
        """Печатает краткий отчёт о состоянии игрока."""
        pass
