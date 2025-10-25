"""Заготовка окон tkinter."""

import tkinter as tk
from tkinter import messagebox, filedialog


class RootWindow:
    """Главное окно приложения."""

    def __init__(self, service):
        self.service = service
        self.root = tk.Tk()
        self.root.title("Data Analyst Tkinter")
        self._build_layout()

    def _build_layout(self):
        """Создаёт базовые элементы интерфейса."""
        self.open_button = tk.Button(self.root, text="Открыть CSV", command=self.choose_file)
        self.open_button.pack(padx=12, pady=12)

        self.info_label = tk.Label(self.root, text="Выберите CSV для анализа")
        self.info_label.pack(padx=12, pady=6)

    def show_welcome(self):
        """Показывает приветствие пользователю."""
        messagebox.showinfo("Data Analyst Tkinter", "Этот шаблон демонстрирует структуру будущего приложения.")

    def start_loop(self):
        """Запускает главный цикл tkinter."""
        self.root.mainloop()

    def choose_file(self):
        """Обработчик выбора файла."""
        path = filedialog.askopenfilename(title="Выбор CSV", filetypes=[("CSV", "*.csv"), ("Все файлы", "*.*")])
        if not path:
            return
        table = self.service.load_dataset(path)
        stats = self.service.calculate_statistics()
        self.info_label.config(text=f"Загружено строк: {len(table._rows)} | Столбцов: {len(stats)}")
