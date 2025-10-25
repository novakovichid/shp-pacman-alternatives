"""Интерфейс командной строки для Data Analyst CLI."""

import argparse

from services.analysis_service import DataAnalysisService


class CommandLineInterface:
    """Обрабатывает аргументы командной строки и выводит сообщения."""

    def __init__(self, service: DataAnalysisService):
        self.service = service
        self.parser = argparse.ArgumentParser(description="Data Analyst CLI")

    def show_welcome(self):
        """Печатает приветственное сообщение."""

        print("Data Analyst CLI — учебный каркас консольного анализатора CSV.")

    def show_placeholder(self):
        """Объясняет, что функциональность ещё не реализована."""

        print("Функциональность утилиты будет добавлена по задачам из каталога tasks/.")

    def run(self):
        """Запускает обработку аргументов и команд."""

        pass
