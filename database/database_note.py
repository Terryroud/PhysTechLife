import sqlite3

class DB_notes:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, article TEXT, date TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT id, title, date FROM notes")
        rows = self.cur.fetchall()
        return rows

    # добавляем новую запись
    def insert(self, title, article, date):
        self.cur.execute("INSERT INTO notes VALUES (NULL,?,?,?)", (title, article, date,))
        self.conn.commit()

    # обновляем информацию о заметке
    def update(self, id, title, article, date):
        self.cur.execute("UPDATE notes SET title=?, article=?, date=? WHERE id=?", (title, article, date, id,))
        self.conn.commit()

    # удаление записи
    def delete(self, id):
        self.cur.execute("DELETE FROM notes WHERE id=?", (id,))
        self.conn.commit()

    # ищем запись по id
    def search_id(self, id):
        self.cur.execute("SELECT * FROM notes WHERE id=?", (id,))
        row = self.cur.fetchall()
        return row

    # ищем запись по названию
    def search(self, title=""):
        self.cur.execute("SELECT * FROM notes WHERE title=?", (title,))
        rows = self.cur.fetchall()
        return rows

db_notes = DB_notes()