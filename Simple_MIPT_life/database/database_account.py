import sqlite3

class DB_account:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, surname TEXT, name TEXT, stud_group TEXT, about TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT id, surname, name, stud_group, about FROM account")
        rows = self.cur.fetchall()
        return rows

    # добавляем новую запись
    def insert(self, surname, name, stud_group, about):
        self.cur.execute("INSERT INTO account VALUES (NULL,?,?,?,?)", (surname, name, stud_group, about,))
        self.conn.commit()
    #
    # # обновляем информацию о заметке
    # def update(self, id, title, article, date):
    #     self.cur.execute("UPDATE notes SET title=?, article=?, date=? WHERE id=?", (title, article, date, id,))
    #     self.conn.commit()
    #
    # # удаление записи
    # def delete(self, id):
    #     self.cur.execute("DELETE FROM notes WHERE id=?", (id,))
    #     self.conn.commit()
    #
    # ищем запись по id
    def search_id(self, id):
        self.cur.execute("SELECT * FROM account WHERE id=?", (id,))
        row = self.cur.fetchall()
        return row
    #
    # # ищем запись по названию
    # def search(self, title=""):
    #     self.cur.execute("SELECT * FROM notes WHERE title=?", (title,))
    #     rows = self.cur.fetchall()
    #     return rows

db_account = DB_account()