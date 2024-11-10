import sqlite3

class DB_study:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS study (id INTEGER PRIMARY KEY, subject TEXT, task INTEGER, week INTEGER, number TEXT, done INTEGER)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT id, subject, task, week, number, done FROM study")
        rows = self.cur.fetchall()
        return rows

    # добавляем новую запись
    def insert(self, subject, task, week, number, done):
        self.cur.execute("INSERT INTO study VALUES (NULL,?,?,?,?,?)", (subject, task, week, number, done))
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
        self.cur.execute("SELECT * FROM study WHERE id=?", (id,))
        row = self.cur.fetchall()
        return row

    # ищем запись по названию
    def search(self, subject=""):
        self.cur.execute("SELECT * FROM study WHERE subject=?", (subject,))
        rows = self.cur.fetchall()
        return rows

db_study = DB_study()