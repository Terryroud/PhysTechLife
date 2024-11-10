from tkinter import StringVar, END, messagebox
import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox
from database.database_account import db_account

class Tab_Account():
    def __init__(self, tab4):
        self._tab4 = tab4

    @property
    def tab4(self):
        return self._tab4

    def show(self, tab4):
        if len(db_account.view()) == 0:
            create_account = customtkinter.CTkToplevel(tab4)
            create_account.title("Новая учетная запись")
            create_account.geometry("800x700")

            p1 = CTkLabel(create_account, text="", font=('Arial', 16))
            p1.grid(row=1, column=1)

            l1 = CTkLabel(create_account, text="Фамилия", font=('Arial', 16))
            l1.grid(row=2, column=1)

            surname_text = StringVar()
            e1 = CTkEntry(create_account, textvariable=surname_text, width=500)
            e1.grid(row=2, column=2)

            p2 = CTkLabel(create_account, text="", font=('Arial', 16))
            p2.grid(row=3, column=1)

            l2 = CTkLabel(create_account, text="Имя", font=('Arial', 16))
            l2.grid(row=4, column=1)

            name_text = StringVar()
            e2 = CTkEntry(create_account, textvariable=name_text, width=500)
            e2.grid(row=4, column=2)

            p3 = CTkLabel(create_account, text="", font=('Arial', 16))
            p3.grid(row=5, column=1)

            l3 = CTkLabel(create_account, text="Группа", font=('Arial', 16))
            l3.grid(row=6, column=1)

            group_text = StringVar()
            e3 = CTkEntry(create_account, textvariable=group_text, width=500)
            e3.grid(row=6, column=2)

            p4 = CTkLabel(create_account, text="", font=('Arial', 16))
            p4.grid(row=7, column=1)

            l4 = CTkLabel(create_account, text="Расскажите о себе", font=('Arial', 16))
            l4.grid(row=8, column=1)

            about_text = CTkTextbox(create_account, width=500, height=400)
            about_text.grid(row=8, column=2)

            p5 = CTkLabel(create_account, text="", font=('Arial', 16))
            p5.grid(row=9, column=1)

            def save_account():
                db_account.insert(surname_text.get(), name_text.get(), group_text.get(), about_text.get("1.0", END).strip())
                create_account.destroy()

            save_button = CTkButton(create_account, text="Сохранить", width=150, height=40, font=('Arial', 16),
                                    command=save_account)
            save_button.grid(row=12, column=2)

        for row in db_account.view():
            l0 = CTkLabel(tab4, text="Основная информация:", font=('Arial', 20, 'bold'), text_color="#7FFFD4")
            l0.pack(pady=10)

            l1 = CTkLabel(tab4, text="Фамилия: " + row[1], font=('Arial', 16))
            l1.pack(pady=10)

            l2 = CTkLabel(tab4, text="Имя: " + row[2], font=('Arial', 16))
            l2.pack(pady=10)

            l3 = CTkLabel(tab4, text="Группа: " + row[3], font=('Arial', 16))
            l3.pack(pady=10)

            l4 = CTkLabel(tab4, text="О себе: " + row[4], font=('Arial', 16))
            l4.pack(pady=10)

            l0 = CTkLabel(tab4, text="Статистика:", font=('Arial', 20, 'bold'), text_color="#7FFFD4")
            l0.pack(pady=10)