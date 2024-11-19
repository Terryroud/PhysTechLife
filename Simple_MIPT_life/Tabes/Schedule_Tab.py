from tkinter import StringVar, END, messagebox

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkTabview, CTkFrame
from database.database_schedule import db_schedule
from static.config import WINDOW_SIZE

class Tab_Schedule():
    def __init__(self, tab_Schedule):
        self._tab_Schedule = tab_Schedule

    @property
    def tab_Schedule(self):
        return self._tab_Schedule

    DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    # Удаление виджетов из окна
    def clear_tab(self, tab):
        for widget in tab.winfo_children():
            widget.destroy()

    # просмотр каждой недели из расписания
    def show_menu(self, tab, tabs, tab_Schedule):
        table_frame = CTkFrame(tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        for day in days:
            Tab_Schedule.show_day(self, day, table_frame, tabs, tab, tab_Schedule)

    # сохранение записи о событии
    def save_note(self, title_text, time_text, tabs, tab, day_num, article_text, event_window, tab_Schedule):
        if title_text and time_text:
            db_schedule.insert(tabs.index(tab) + 1, day_num, title_text.get(),
                               time_text.get(), article_text.get("1.0", END).strip())
            event_window.destroy()
            Tab_Schedule.clear_tab(self, tab)
            Tab_Schedule.show_menu(self, tab, tabs, tab_Schedule)
        else:
            messagebox.showwarning("Предупреждение", "Заполните все поля!")

    # обработчик нажатия на кнопку «Добавить»
    def create_new(self, day_num, tab, tab_Schedule, tabs):
        event_window = customtkinter.CTkToplevel(tab_Schedule)
        event_window.title("Новая запись")
        event_window.geometry(WINDOW_SIZE)

        title_label = CTkLabel(event_window, text="Название", font=('Arial', 14))
        title_label.pack(pady=10)

        title_text = StringVar()
        title_entry = CTkEntry(event_window, textvariable=title_text, width=500)
        title_entry.pack(pady=10)

        time_label = CTkLabel(event_window, text="Время события", font=('Arial', 14))
        time_label.pack(pady=10)

        time_text = StringVar()
        time_entry = CTkEntry(event_window, textvariable=time_text, width=500)
        time_entry.pack(pady=10)

        describe_label = CTkLabel(event_window, text="Описание", font=('Arial', 14))
        describe_label.pack(pady=10)

        article_text = CTkTextbox(event_window, width=500, height=350)
        article_text.pack(pady=10)

        save_button = CTkButton(event_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16),
                                command=lambda : Tab_Schedule.save_note(self, title_text, time_text, tabs, tab, day_num, article_text, event_window, tab_Schedule))
        save_button.pack(pady=20)

    # обработчик нажатия на кнопку «Удалить»
    def delete_command(self, tab, tab_Schedule, tabs):
        event_window = customtkinter.CTkToplevel(tab_Schedule)
        event_window.title("Удаление")
        event_window.geometry(WINDOW_SIZE)

        warning_label = CTkLabel(event_window, text="Укажите точное название записи, которую хотите удалить:",
                                 font=('Arial', 14))
        warning_label.pack(pady=10)

        title_text = StringVar()
        e1 = CTkEntry(event_window, textvariable=title_text, width=500)
        e1.pack(pady=10)

        save_button = CTkButton(event_window, text="Удалить", width=150, height=40, font=('Arial', 16),
                                command=lambda : Tab_Schedule.delete_note(self, title_text, event_window, tab, tabs, tab_Schedule))
        save_button.pack(pady=20)

    # удаление выбранной записи о событии
    def delete_note(self, title_text, event_window, tab, tabs, tab_Schedule):
        try:
            del_id = db_schedule.search_title(title_text.get())[0][0]
            db_schedule.delete(del_id)
            event_window.destroy()
            Tab_Schedule.clear_tab(self, tab)
            Tab_Schedule.show_menu(self, tab, tabs, tab_Schedule)
        except:
            messagebox.showwarning("Предупреждение", "Такой записи не найдено, повторите попытку")

    # отображение отдельного дня недели в расписании как отдельной ячейки
    def show_day(self, day, table_frame, tabs, tab, tab_Schedule):
        i = Tab_Schedule.DAYS.index(day)
        label = CTkLabel(table_frame, text=day)
        label.grid(row=0, column=i, padx=5, pady=5)

        index = 0
        for row in db_schedule.search_week(tabs.index(tab) + 1):
            if row[2] == i + 1:
                event_listbox = CTkLabel(table_frame, text=f'Название: {row[3]}\nВремя: {row[4]}\nОписание: {row[5]}')
                event_listbox.grid(row=1 + index, column=i, padx=5, pady=5)
                index += 1

        btn_add_event = CTkButton(table_frame, text="Добавить событие", command=lambda: Tab_Schedule.create_new(self, i + 1, tab, tab_Schedule, tabs))
        btn_add_event.grid(row=3 + index, column=i, padx=5, pady=(0, 5))

        btn_remove_event = CTkButton(table_frame, text="Удалить событие", command=lambda: Tab_Schedule.delete_command(self, tab, tab_Schedule, tabs))
        btn_remove_event.grid(row=4 + index, column=i, padx=5, pady=(0, 5))

    # отображение всей графики вкладки "Расписание"
    def show(self, tab_Schedule):
        notebook = CTkTabview(tab_Schedule)
        notebook.pack(side="top", fill="both")

        tab_first_week = notebook.add("Неделя 1")
        tab_second_week = notebook.add("Неделя 2")
        tab_third_week = notebook.add("Неделя 3")
        tab_fourth_week = notebook.add("Неделя 4")
        notebook.pack(side="top", fill="x")

        tabs = [tab_first_week, tab_second_week, tab_third_week, tab_fourth_week]
        for tab in tabs:
            Tab_Schedule.show_menu(self, tab, tabs, tab_Schedule)
