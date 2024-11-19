from tkinter import messagebox

import customtkinter
from customtkinter import CTkTabview
from CTkListbox import *

from Tabes.Account_Tab import Tab_Account
from Tabes.Notes_Tab import Tab_Notes
from Tabes.Schedule_Tab import Tab_Schedule
from Tabes.Study_Tab import Tab_Study

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")

    # создание основного окна
    window = customtkinter.CTk()
    window.title("PhysTech")
    window.geometry("1100x600")
    notebook = CTkTabview(window)
    notebook.pack(side="top",fill="both")

    # создание 4х основных вкладок
    tab_Schedule = notebook.add("Расписание")
    tab_Study = notebook.add("Обучение")
    tab_Notes = notebook.add("Заметки")
    tab_Account = notebook.add("Личный кабинет")
    notebook.pack(side="top",fill="x")

    # отображение вкладки "Заметки"
    list_notes = CTkListbox(tab_Notes, height=500, width=800)
    tab_notes = Tab_Notes(tab_Notes, list_notes)
    tab_notes.show(tab_Notes, list_notes)

    # отображение вкладки "Личный Кабинет"
    tab_account = Tab_Account(tab_Account)
    tab_account.show(tab_Account)

    # отображение вкладки "Обучение"
    tab_study = Tab_Study(tab_Study)
    tab_study.show(tab_Study)

    # отображение вкладки "Расписание"
    tab_schedule = Tab_Schedule(tab_Schedule)
    tab_schedule.show(tab_Schedule)

    # обработка закрытие окна
    def on_closing():
        if messagebox.askokcancel("", "Закрыть программу?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
