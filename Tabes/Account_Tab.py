from tkinter import StringVar, END
import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox
from database.database_account import db_account
from static.config import WINDOW_SIZE

class Tab_Account():
    def __init__(self, tab_Account):
        self._tab_Account = tab_Account

    @property
    def tab_Account(self):
        return self._tab_Account

    # первичное сохранение данных пользователя после регистрации
    def save_account(self, surname_text, name_text, group_text, about_text, create_account):
        db_account.insert(surname_text.get(), name_text.get(), group_text.get(), about_text.get("1.0", END).strip())
        create_account.destroy()

    # отображение всей графики вкладки "Личный Кабинет"
    def show(self, tab_Account):
        if len(db_account.view()) == 0:
            create_account = customtkinter.CTkToplevel(tab_Account)
            create_account.title("Новая учетная запись")
            create_account.geometry(WINDOW_SIZE)

            free_label = CTkLabel(create_account, text="", font=('Arial', 16))
            free_label.grid(row=1, column=1)

            surname_label = CTkLabel(create_account, text="Фамилия", font=('Arial', 16))
            surname_label.grid(row=2, column=1)

            surname_text = StringVar()
            surname_entry = CTkEntry(create_account, textvariable=surname_text, width=500)
            surname_entry.grid(row=2, column=2)

            free_label = CTkLabel(create_account, text="", font=('Arial', 16))
            free_label.grid(row=3, column=1)

            name_label = CTkLabel(create_account, text="Имя", font=('Arial', 16))
            name_label.grid(row=4, column=1)

            name_text = StringVar()
            name_entry = CTkEntry(create_account, textvariable=name_text, width=500)
            name_entry.grid(row=4, column=2)

            free_label = CTkLabel(create_account, text="", font=('Arial', 16))
            free_label.grid(row=5, column=1)

            group_label = CTkLabel(create_account, text="Группа", font=('Arial', 16))
            group_label.grid(row=6, column=1)

            group_text = StringVar()
            group_entry = CTkEntry(create_account, textvariable=group_text, width=500)
            group_entry.grid(row=6, column=2)

            free_label = CTkLabel(create_account, text="", font=('Arial', 16))
            free_label.grid(row=7, column=1)

            about_label = CTkLabel(create_account, text="Расскажите о себе", font=('Arial', 16))
            about_label.grid(row=8, column=1)

            about_text = CTkTextbox(create_account, width=500, height=400)
            about_text.grid(row=8, column=2)

            free_label = CTkLabel(create_account, text="", font=('Arial', 16))
            free_label.grid(row=9, column=1)

            save_button = CTkButton(create_account, text="Сохранить", width=150, height=40, font=('Arial', 16),
                                    command= lambda : Tab_Account.save_account(self, surname_text, name_text, group_text, about_text, create_account))
            save_button.grid(row=12, column=2)

        for row in db_account.view():
            main_label = CTkLabel(tab_Account, text="Основная информация:", font=('Arial', 20, 'bold'), text_color="#7FFFD4")
            main_label.pack(pady=10)

            surname_label = CTkLabel(tab_Account, text=f"Фамилия: {row[1]}", font=('Arial', 16))
            surname_label.pack(pady=10)

            name_label = CTkLabel(tab_Account, text=f"Имя: {row[2]}", font=('Arial', 16))
            name_label.pack(pady=10)

            group_label = CTkLabel(tab_Account, text=f"Группа: {row[3]}", font=('Arial', 16))
            group_label.pack(pady=10)

            about_label = CTkLabel(tab_Account, text=f"О себе: {row[4]}", font=('Arial', 16))
            about_label.pack(pady=10)

            statistic_label = CTkLabel(tab_Account, text="Статистика:", font=('Arial', 20, 'bold'), text_color="#7FFFD4")
            statistic_label.pack(pady=10)