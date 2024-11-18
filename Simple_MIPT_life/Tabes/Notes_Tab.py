from tkinter import StringVar, END, messagebox
import datetime
from database.database_note import db_notes

import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkTextbox
from static.config import WINDOW_SIZE

class Tab_Notes():
    def __init__(self, tab_Notes, list_notes):
        self._tab_Notes = tab_Notes
        self._list_notes = list_notes

    @property
    def tab_Notes(self):
        return self._tab_Notes

    @property
    def list_notes(self):
        return self._list_notes

    # обработчик нажатия на кнопку «Посмотреть всё»
    def view_command(self, list_notes):
        list_notes.delete(0, END)
        for row in db_notes.view():
            list_notes.insert(END, row)

    # функция для отслеживания выбранной позиции
    def get_selected_row(self, list_notes):
        index = list_notes.curselection()
        selected_tuple = db_notes.search_id(list_notes.get(index)[0])[0]
        return selected_tuple

    # функция для сохранения заметки
    def save_note(self, title_text, article_text, list_notes, note_window):
        if title_text:
            date_text = str(datetime.date.today())
            db_notes.insert(title_text.get(), article_text.get("1.0", END).strip(), date_text)
            Tab_Notes.view_command(self, list_notes)
            note_window.destroy()
        else:
            messagebox.showwarning("Предупреждение", "Введите текст заметки!")

    # обработчик нажатия на кнопку «Добавить»
    def create_new(self, tab_Notes, list_notes):
        note_window = customtkinter.CTkToplevel(tab_Notes)
        note_window.title("Новая заметка")
        note_window.geometry(WINDOW_SIZE)

        title_label = CTkLabel(note_window, text="Название", font=('Arial', 14))
        title_label.pack(pady=10)

        title_text = StringVar()
        title_entry = CTkEntry(note_window, textvariable=title_text, width=500)
        title_entry.pack(pady=10)

        text_label = CTkLabel(note_window, text="Текст заметки", font=('Arial', 14))
        text_label.pack(pady=10)

        article_text = CTkTextbox(note_window, width=500, height=400)
        article_text.pack(pady=10)

        save_button = CTkButton(note_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.save_note(self, title_text, article_text, list_notes, note_window))
        save_button.pack(pady=20)

    # обработчик нажатия на кнопку «Удалить»
    def delete_command(self, list_notes):
        db_notes.delete(Tab_Notes.get_selected_row(self, list_notes)[0])
        index = 0
        flag = True

        while flag:
            try:
                db_notes.update(index + 1, list_notes.get(index)[1], db_notes.search_id(list_notes.get(index)[0])[0][2], list_notes.get(index)[2])
                index += 1
            except:
                flag = False
        Tab_Notes.view_command(self, list_notes)

    # обновление списка заметок после совершения действий над ним
    def update_command(self, list_notes, title_text, article_text, note_window):
        date_text = str(datetime.date.today())
        db_notes.update(Tab_Notes.get_selected_row(self, list_notes)[0], title_text.get("1.0", END).strip(), article_text.get("1.0", END).strip(), date_text)
        Tab_Notes.view_command(self, list_notes)
        note_window.destroy()

    # просмотр и редактирование выбранной заметки
    def view_this(self, tab_Notes, list_notes):
        note_window = customtkinter.CTkToplevel(tab_Notes)
        note_window.title(Tab_Notes.get_selected_row(self, list_notes)[1])
        note_window.geometry(WINDOW_SIZE)

        title_label = CTkLabel(note_window, text="Название", font=('Arial', 14))
        title_label.pack(pady=10)

        title_text = CTkTextbox(note_window, width=500, height=40)
        title_text.pack(pady=10)
        title_text.insert(END, Tab_Notes.get_selected_row(self, list_notes)[1])

        text_label = CTkLabel(note_window, text="Текст заметки", font=('Arial', 14))
        text_label.pack(pady=10)

        article_text = CTkTextbox(note_window, width=500, height=400)
        article_text.pack(pady=10)
        article_text.insert(END, Tab_Notes.get_selected_row(self, list_notes)[2])

        save_button = CTkButton(note_window, text="Сохранить заметку", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.update_command(self, list_notes, title_text, article_text, note_window))
        save_button.pack(pady=20)

    # отображение всей графики вкладки "Заметки"
    def show(self, tab_Notes, list_notes):
        list_notes.grid(row=2, column=0, rowspan=6, columnspan=10)

        # list_notes.bind('<<ListboxSelect>>', Tab_Notes.get_selected_row(self, list_notes))

        Tab_Notes.view_command(self, list_notes)

        free_label = CTkLabel(tab_Notes, text="            ", font=('Arial', 16))
        free_label.grid(row=2, column=11)

        view_all_label = CTkButton(tab_Notes, text="Посмотреть все", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.view_command(self, list_notes))
        view_all_label.grid(row=2, column=12)

        change_label = CTkButton(tab_Notes, text="Изменить", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.view_this(self, tab_Notes, list_notes))
        change_label.grid(row=3, column=12)

        add_label = CTkButton(tab_Notes, text="Добавить", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.create_new(self, tab_Notes, list_notes))
        add_label.grid(row=4, column=12)

        remove_label = CTkButton(tab_Notes, text="Удалить", width=150, height=40, font=('Arial', 16), command=lambda : Tab_Notes.delete_command(self, list_notes))
        remove_label.grid(row=5, column=12)
