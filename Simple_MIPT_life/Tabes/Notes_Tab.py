from tkinter import StringVar, END, messagebox
import datetime
from database.database_note import db_notes

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox


class Tab_notes():
    def __init__(self, tab3, list_notes):
        self._tab3 = tab3
        self._list_notes = list_notes

    @property
    def tab3(self):
        return self._tab3

    @property
    def list_notes(self):
        return self._list_notes

    def show(self, tab3, list_notes):
        list_notes.grid(row=2, column=0, rowspan=6, columnspan=10)

        def get_selected_row(event):
            global selected_tuple
            index = list_notes.curselection()
            selected_tuple = db_notes.search_id(list_notes.get(index)[0])[0]

        list_notes.bind('<<ListboxSelect>>', get_selected_row)

        # обработчик нажатия на кнопку «Посмотреть всё»
        def view_command():
            list_notes.delete(0, END)
            for row in db_notes.view():
                list_notes.insert(END, row)

        view_command()

        # обработчик нажатия на кнопку «Добавить»
        def create_new():
            note_window = customtkinter.CTkToplevel(tab3)
            note_window.title("Новая заметка")
            note_window.geometry("800x700")

            l1 = CTkLabel(note_window, text="Название", font=('Arial', 14))
            l1.pack(pady=10)

            title_text = StringVar()
            e1 = CTkEntry(note_window, textvariable=title_text, width=500)
            e1.pack(pady=10)

            l2 = CTkLabel(note_window, text="Текст заметки", font=('Arial', 14))
            l2.pack(pady=10)

            article_text = CTkTextbox(note_window, width=500, height=400)
            article_text.pack(pady=10)

            def save_note():
                if title_text:
                    date_text = str(datetime.date.today())
                    db_notes.insert(title_text.get(), article_text.get("1.0", END).strip(), date_text)
                    view_command()
                    note_window.destroy()
                else:
                    messagebox.showwarning("Предупреждение", "Введите текст заметки!")

            save_button = CTkButton(note_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16), command=save_note)
            save_button.pack(pady=20)

        # обработчик нажатия на кнопку «Удалить»
        def delete_command():
            db_notes.delete(selected_tuple[0])
            index = 0
            flag = True

            while flag:
                try:
                    db_notes.update(index + 1, list_notes.get(index)[1], db_notes.search_id(list_notes.get(index)[0])[0][2], list_notes.get(index)[2])
                    index += 1
                except:
                    flag = False
            view_command()

        def view_this():
            note_window = customtkinter.CTkToplevel(tab3)
            note_window.title(selected_tuple[1])
            note_window.geometry("800x700")

            l1 = CTkLabel(note_window, text="Название", font=('Arial', 14))
            l1.pack(pady=10)

            title_text = CTkTextbox(note_window, width=500, height=40)
            title_text.pack(pady=10)
            title_text.insert(END, selected_tuple[1])

            l2 = CTkLabel(note_window, text="Текст заметки", font=('Arial', 14))
            l2.pack(pady=10)

            article_text = CTkTextbox(note_window, width=500, height=400)
            article_text.pack(pady=10)
            article_text.insert(END, selected_tuple[2])

            def update_command():
                date_text = str(datetime.date.today())
                db_notes.update(selected_tuple[0], title_text.get("1.0", END).strip(), article_text.get("1.0", END).strip(), date_text)
                view_command()
                note_window.destroy()

            save_button = CTkButton(note_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16), command=update_command)
            save_button.pack(pady=20)

        p0 = CTkLabel(tab3, text="            ", font=('Arial', 16))
        p0.grid(row=2, column=11)

        b1 = CTkButton(tab3, text="Посмотреть все", width=150, height=40, font=('Arial', 16), command=view_command)
        b1.grid(row=2, column=12)

        b2 = CTkButton(tab3, text="Изменить", width=150, height=40, font=('Arial', 16), command=view_this)
        b2.grid(row=3, column=12)

        b3 = CTkButton(tab3, text="Добавить", width=150, height=40, font=('Arial', 16), command=create_new)
        b3.grid(row=4, column=12)

        b5 = CTkButton(tab3, text="Удалить", width=150, height=40, font=('Arial', 16), command=delete_command)
        b5.grid(row=5, column=12)
