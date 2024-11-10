import sqlite3

from tkinter import messagebox

import customtkinter
from customtkinter import CTkTabview
from CTkListbox import *

from Tabes.Account_Tab import Tab_Account
from Tabes.Notes_Tab import Tab_notes
from Tabes.Schedule_Tab import ScheduleApp
from Tabes.Study_Tab import Tab_Study

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")

    window = customtkinter.CTk()
    window.title("PhysTech")
    window.geometry("1100x600")
    notebook = CTkTabview(window)
    notebook.pack(side="top",fill="both")

    tab1 = notebook.add("Расписание")
    tab2 = notebook.add("Обучение")
    tab3 = notebook.add("Заметки")
    tab4 = notebook.add("Личный кабинет")
    notebook.pack(side="top",fill="x")

    list_notes = CTkListbox(tab3, height=500, width=800)
    tab_notes = Tab_notes(tab3, list_notes)
    tab_notes.show(tab3, list_notes)

    tab_account = Tab_Account(tab4)
    tab_account.show(tab4)

    tab_study = Tab_Study(tab2)
    tab_study.show(tab2)

    tab_schedule = ScheduleApp(tab1)
    tab_schedule.show(tab1)

    # обрабатываем закрытие окна
    def on_closing():
        if messagebox.askokcancel("", "Закрыть программу?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()