from tkinter import StringVar, messagebox

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTabview, CTkRadioButton, TOP
from database.database_study import db_study
from static.config import WINDOW_SIZE

class Tab_Study():
    def __init__(self, tab_Study):
        self._tab_Study = tab_Study

    @property
    def tab_Study(self):
        return self._tab_Study

    OPTIONS = ["Матан", "Ангем", "Общесос", "Алктг"]

    # изменениe состояния кнопки
    def change_done(self, button_main):
        if button_main.cget("text") == "Сделано!":
            button_main.configure(bg_color='#696969', text="Не сделано.")
        else:
            button_main.configure(bg_color='#00FF7F', text="Сделано!")

    def Tab_Subject(self, tab_Subject, subject_name):
        step = 0

        for row in db_study.search(subject_name):
            free_label = CTkLabel(tab_Subject, text="      ", font=('Arial', 16))
            free_label.grid(row=1 + step, column=1)

            free_label = CTkLabel(tab_Subject, text="      ", font=('Arial', 16))
            free_label.grid(row=2 + step, column=1)

            task_label = CTkLabel(tab_Subject,
                                  text=f'Задание №{str(row[2])}. Неделя №{str(row[3])}. Задача номер {row[4]}',
                                  font=('Arial', 16))
            task_label.grid(row=2 + step, column=2)

            free_label = CTkLabel(tab_Subject, text="      ", font=('Arial', 16))
            free_label.grid(row=2 + step, column=3)

            button_main = CTkButton(tab_Subject, fg_color='#696969', text="Не сделано.", width=80, command=lambda : Tab_Study.change_done(self, button_main))
            button_main.grid(row=2 + step, column=4)

            step += 2

    # сохранение добавленного задания и обновление всех вкладок
    def save_task(self, task_number, week_number, small_task_number, selected_option, task_window, tab_Calculus, tab_Angem, tab_Physics, tab_Olmath):
        if task_number and week_number and small_task_number:
            db_study.insert(str(selected_option.get()), int(task_number.get()), int(week_number.get()),
                            str(small_task_number.get()), 0)
            task_window.destroy()
            Tab_Study.Tab_Subject(self, tab_Calculus, "Матан")
            Tab_Study.Tab_Subject(self, tab_Angem, "Ангем")
            Tab_Study.Tab_Subject(self, tab_Physics, "Общесос")
            Tab_Study.Tab_Subject(self, tab_Olmath, "Алктг")
        else:
            messagebox.showwarning("Предупреждение", "Заполните все поля!")

    # обработчик нажатия на кнопку «Добавить»
    def create_new(self, tab_Study, tab_Calculus, tab_Angem, tab_Physics, tab_Olmath):
        task_window = customtkinter.CTkToplevel(tab_Study)
        task_window.title("Новая задача")
        task_window.geometry(WINDOW_SIZE)

        subject_label = CTkLabel(task_window, text="Предмет", font=('Arial', 14))
        subject_label.pack(pady=10)

        selected_option = StringVar(value="")

        for option in Tab_Study.OPTIONS:
            radio_button = CTkRadioButton(task_window, text=option, variable=selected_option, value=option)
            radio_button.pack(pady=5)

        task_label = CTkLabel(task_window, text="Задание. Укажите число:", font=('Arial', 14))
        task_label.pack(pady=10)

        task_number = StringVar()
        task_entry = CTkEntry(task_window, textvariable=task_number, width=500)
        task_entry.pack(pady=10)

        week_label = CTkLabel(task_window, text="Неделя. Укажите число:", font=('Arial', 14))
        week_label.pack(pady=10)

        week_number = StringVar()
        week_entry = CTkEntry(task_window, textvariable=week_number, width=500)
        week_entry.pack(pady=10)

        number_label = CTkLabel(task_window, text="Номер упражнения:", font=('Arial', 14))
        number_label.pack(pady=10)

        small_task_number = StringVar()
        number_entry = CTkEntry(task_window, textvariable=small_task_number, width=500)
        number_entry.pack(pady=10)

        save_button = CTkButton(task_window, text="Сохранить задачу", width=150, height=40, font=('Arial', 16),
                                command=lambda : Tab_Study.save_task(self, task_number, week_number, small_task_number,
                                selected_option, task_window, tab_Calculus, tab_Angem, tab_Physics, tab_Olmath))
        save_button.pack(pady=20)

    # отображение всей графики вкладки "Обучение"
    def show(self, tab_Study):
        notebook = CTkTabview(tab_Study)
        notebook.pack(side="top", fill="both")

        tab_Calculus = notebook.add("Матан")
        tab_Angem = notebook.add("Ангем")
        tab_Physics = notebook.add("Общесос")
        tab_Olmath = notebook.add("Алктг")
        notebook.pack(side="top", fill="x")

        Tab_Study.Tab_Subject(self, tab_Calculus, "Матан")
        Tab_Study.Tab_Subject(self, tab_Angem, "Ангем")
        Tab_Study.Tab_Subject(self, tab_Physics, "Общесос")
        Tab_Study.Tab_Subject(self, tab_Olmath, "Алктг")

        button_new = CTkButton(tab_Study, text="Добавить новую задачу", width=150, height=40, font=('Arial', 14),
                               command=lambda : Tab_Study.create_new(self, tab_Study, tab_Calculus, tab_Angem, tab_Physics, tab_Olmath))

        button_new.pack(side=TOP, pady=10)
