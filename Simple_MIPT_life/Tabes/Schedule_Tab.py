from tkinter import StringVar, END, messagebox

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkTabview, CTkFrame

from database.database_schedule import db_schedule


class ScheduleApp():
    def __init__(self, tab1):
        self._tab1 = tab1

    @property
    def tab1(self):
        return self._tab1

    def show(self, tab1):
        notebook = CTkTabview(tab1)
        notebook.pack(side="top", fill="both")

        tab11 = notebook.add("Неделя 1")
        tab12 = notebook.add("Неделя 2")
        tab13 = notebook.add("Неделя 3")
        tab14 = notebook.add("Неделя 4")
        notebook.pack(side="top", fill="x")

        def clear_tab(tab):
            for widget in tab.winfo_children():
                widget.destroy()  # Удаляет виджет из окна

        tabs = [tab11, tab12, tab13, tab14]
        for tab in tabs:
            def show_min(tab):
                table_frame = CTkFrame(tab)
                table_frame.pack(expand=True, fill="both", padx=10, pady=10)

                days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
                for day in days:
                    def show_day(day):
                        i = days.index(day)
                        label = CTkLabel(table_frame, text=day)
                        label.grid(row=0, column=i, padx=5, pady=5)

                        index = 0
                        for row in db_schedule.search_week(tabs.index(tab) + 1):
                            if row[2] == i + 1:
                                event_listbox = CTkLabel(table_frame, text='Название: ' + row[3] + '\nВремя: ' + row[4] + '\nОписание: ' + row[5])
                                event_listbox.grid(row=1 + index, column=i, padx=5, pady=5)
                                index += 1

                        btn_add_event = CTkButton(table_frame, text="Добавить событие", command=lambda : create_new(i + 1, tab))
                        btn_add_event.grid(row=3 + index, column=i, padx=5, pady=(0, 5))

                        btn_remove_event = CTkButton(table_frame, text="Удалить событие", command=lambda : delete_command(tab))
                        btn_remove_event.grid(row=4 + index, column=i, padx=5, pady=(0, 5))

                    show_day(day)

            show_min(tab)

        # обработчик нажатия на кнопку «Добавить»
        def create_new(day_num, tab):
            event_window = customtkinter.CTkToplevel(tab1)
            event_window.title("Новая запись")
            event_window.geometry("800x700")

            l1 = CTkLabel(event_window, text="Название", font=('Arial', 14))
            l1.pack(pady=10)

            title_text = StringVar()
            e1 = CTkEntry(event_window, textvariable=title_text, width=500)
            e1.pack(pady=10)

            l3 = CTkLabel(event_window, text="Время события", font=('Arial', 14))
            l3.pack(pady=10)

            time_text = StringVar()
            e3 = CTkEntry(event_window, textvariable=time_text, width=500)
            e3.pack(pady=10)

            l2 = CTkLabel(event_window, text="Описание", font=('Arial', 14))
            l2.pack(pady=10)

            article_text = CTkTextbox(event_window, width=500, height=350)
            article_text.pack(pady=10)

            def save_note():
                if title_text and time_text:
                    db_schedule.insert(tabs.index(tab) + 1, day_num, title_text.get(),
                                       time_text.get(), article_text.get("1.0", END).strip())
                    event_window.destroy()
                    clear_tab(tab)
                    show_min(tab)
                else:
                    messagebox.showwarning("Предупреждение", "Заполните все поля!")

            save_button = CTkButton(event_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16),
                                    command=save_note)
            save_button.pack(pady=20)

        # обработчик нажатия на кнопку «Удалить»
        def delete_command(tab):
            event_window = customtkinter.CTkToplevel(tab1)
            event_window.title("Удаление")
            event_window.geometry("800x300")

            l1 = CTkLabel(event_window, text="Укажите точное название записи, которую хотите удалить:", font=('Arial', 14))
            l1.pack(pady=10)

            title_text = StringVar()
            e1 = CTkEntry(event_window, textvariable=title_text, width=500)
            e1.pack(pady=10)

            def delete_note():
                try:
                    del_id = db_schedule.search_title(title_text.get())[0][0]
                    db_schedule.delete(del_id)
                    event_window.destroy()
                    clear_tab(tab)
                    show_min(tab)
                except:
                    messagebox.showwarning("Предупреждение", "Такой записи не найдено, повторите попытку")

            save_button = CTkButton(event_window, text="Удалить", width=150, height=40, font=('Arial', 16),command=delete_note)
            save_button.pack(pady=20)
