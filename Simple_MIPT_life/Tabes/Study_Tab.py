from tkinter import StringVar, messagebox

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkTabview, CTkRadioButton, TOP

from database.database_study import db_study

class Tab_Study():
    def __init__(self, tab2):
        self._tab2 = tab2

    @property
    def tab2(self):
        return self._tab2

    def show(self, tab2):
        notebook = CTkTabview(tab2)
        notebook.pack(side="top", fill="both")

        tab21 = notebook.add("Матан")
        tab22 = notebook.add("Ангем")
        tab23 = notebook.add("Общесос")
        tab24 = notebook.add("Алктг")
        notebook.pack(side="top", fill="x")

        def change_done_all(button1):
            if button1.cget("text") == "Сделано!":
                button1.configure(bg_color='#696969', text="Не сделано.")
            else:
                button1.configure(bg_color='#00FF7F', text="Сделано!")

        def Tab_Matan(tab21):
            def change_done():
                change_done_all(button1)

            step = 0

            for row in db_study.search("Матан"):
                p0 = CTkLabel(tab21, text="      ", font=('Arial', 16))
                p0.grid(row=1 + step, column=1)

                p1 = CTkLabel(tab21, text="      ", font=('Arial', 16))
                p1.grid(row=2 + step, column=1)

                l1 = CTkLabel(tab21, text= 'Задание №' + str(row[2]) + '. Неделя №' + str(row[3]) + ': номер ' + row[4], font=('Arial', 16))
                l1.grid(row=2 + step, column=2)

                p2 = CTkLabel(tab21, text="      ", font=('Arial', 16))
                p2.grid(row=2 + step, column=3)

                button1 = CTkButton(tab21, fg_color='#696969', text="Не сделано.", width=80, command=change_done)
                button1.grid(row=2 + step, column=4)

                step += 2

        def Tab_Angem(tab22):
            def change_done():
                change_done_all(button1)

            step = 0

            for row in db_study.search("Ангем"):
                p0 = CTkLabel(tab22, text="      ", font=('Arial', 16))
                p0.grid(row=1 + step, column=1)

                p1 = CTkLabel(tab22, text="      ", font=('Arial', 16))
                p1.grid(row=2 + step, column=1)

                l1 = CTkLabel(tab22, text= 'Задание №' + str(row[2]) + '. Неделя №' + str(row[3]) + ': номер ' + row[4], font=('Arial', 16))
                l1.grid(row=2 + step, column=2)

                p2 = CTkLabel(tab22, text="      ", font=('Arial', 16))
                p2.grid(row=2 + step, column=3)

                button1 = CTkButton(tab22, fg_color='#696969', text="Не сделано.", width=80, command=change_done)
                button1.grid(row=2 + step, column=4)

                step += 2

        def Tab_Physics(tab23):
            def change_done():
                change_done_all(button1)

            step = 0

            for row in db_study.search("Общесос"):
                p0 = CTkLabel(tab23, text="      ", font=('Arial', 16))
                p0.grid(row=1 + step, column=1)

                p1 = CTkLabel(tab23, text="      ", font=('Arial', 16))
                p1.grid(row=2 + step, column=1)

                l1 = CTkLabel(tab23, text= 'Задание №' + str(row[2]) + '. Неделя №' + str(row[3]) + ': номер ' + row[4], font=('Arial', 16))
                l1.grid(row=2 + step, column=2)

                p2 = CTkLabel(tab23, text="      ", font=('Arial', 16))
                p2.grid(row=2 + step, column=3)

                button1 = CTkButton(tab23, fg_color='#696969', text="Не сделано.", width=80, command=change_done)
                button1.grid(row=2 + step, column=4)

                step += 2

        def Tab_Alktg(tab24):
            def change_done():
                change_done_all(button1)

            step = 0

            for row in db_study.search("Алктг"):
                p0 = CTkLabel(tab24, text="      ", font=('Arial', 16))
                p0.grid(row=1 + step, column=1)

                p1 = CTkLabel(tab24, text="      ", font=('Arial', 16))
                p1.grid(row=2 + step, column=1)

                l1 = CTkLabel(tab24, text= 'Задание №' + str(row[2]) + '. Неделя №' + str(row[3]) + ': номер ' + row[4], font=('Arial', 16))
                l1.grid(row=2 + step, column=2)

                p2 = CTkLabel(tab24, text="      ", font=('Arial', 16))
                p2.grid(row=2 + step, column=3)

                button1 = CTkButton(tab24, fg_color='#696969', text="Не сделано.", width=80, command=change_done)
                button1.grid(row=2 + step, column=4)

                step += 2

        Tab_Matan(tab21)
        Tab_Angem(tab22)
        Tab_Physics(tab23)
        Tab_Alktg(tab24)

        # обработчик нажатия на кнопку «Добавить»
        def create_new():
            task_window = customtkinter.CTkToplevel(tab2)
            task_window.title("Новая задача")
            task_window.geometry("800x700")

            l1 = CTkLabel(task_window, text="Предмет", font=('Arial', 14))
            l1.pack(pady=10)

            options = ["Матан", "Ангем", "Общесос", "Алктг"]
            selected_option = StringVar(value="")

            for option in options:
                radio_button = CTkRadioButton(task_window, text=option, variable=selected_option, value=option)
                radio_button.pack(pady=5)

            l2 = CTkLabel(task_window, text="Задание. Укажите число:", font=('Arial', 14))
            l2.pack(pady=10)

            task_number = StringVar()
            e2 = CTkEntry(task_window, textvariable=task_number, width=500)
            e2.pack(pady=10)

            l3 = CTkLabel(task_window, text="Неделя. Укажите число:", font=('Arial', 14))
            l3.pack(pady=10)

            week_number = StringVar()
            e3 = CTkEntry(task_window, textvariable=week_number, width=500)
            e3.pack(pady=10)

            l4 = CTkLabel(task_window, text="Номер упражнения:", font=('Arial', 14))
            l4.pack(pady=10)

            small_task_number = StringVar()
            e4 = CTkEntry(task_window, textvariable=small_task_number, width=500)
            e4.pack(pady=10)

            def save_task():
                if task_number and week_number and small_task_number:
                    db_study.insert(str(selected_option.get()), int(task_number.get()), int(week_number.get()), str(small_task_number.get()), 0)
                    task_window.destroy()
                    Tab_Matan(tab21)
                    Tab_Angem(tab22)
                    Tab_Physics(tab23)
                    Tab_Alktg(tab24)
                else:
                    messagebox.showwarning("Предупреждение", "Заполните все поля!")

            save_button = CTkButton(task_window, text="Сохранить задачу", width=150, height=40, font=('Arial', 16), command=save_task)
            save_button.pack(pady=20)

        b_new = CTkButton(tab2, text="Добавить новую задачу", width=150, height=40, font=('Arial', 14), command=create_new)
        b_new.pack(side=TOP, pady=10)
