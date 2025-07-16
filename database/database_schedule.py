import sqlite3

class DB_schedule:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS schedule (id INTEGER PRIMARY KEY, week INTEGER, day INTEGER, title TEXT, article TEXT, time TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT id, week, day, title, article, time FROM schedule")
        rows = self.cur.fetchall()
        return rows

    # добавляем новую запись
    def insert(self, week, day, title, article, time):
        self.cur.execute("INSERT INTO schedule VALUES (NULL,?,?,?,?,?)", (week, day, title, article, time))
        self.conn.commit()
    #
    # обновляем информацию о заметке
    def update(self, id, week, day, title, article, time):
        self.cur.execute("UPDATE schedule SET week=?, day=?, title=?, article=?, time=? WHERE id=?", (week, day, title, article, time, id))
        self.conn.commit()

    # удаление записи
    def delete(self, id):
        self.cur.execute("DELETE FROM schedule WHERE id=?", (id,))
        self.conn.commit()
    #
    # ищем запись по id
    def search_id(self, id):
        self.cur.execute("SELECT * FROM schedule WHERE id=?", (id,))
        row = self.cur.fetchall()
        return row
    #
    # ищем запись по неделе
    def search_week(self, week):
        self.cur.execute("SELECT * FROM schedule WHERE week=?", (week,))
        rows = self.cur.fetchall()
        return rows

    # ищем запись по названию
    def search_title(self, title):
        self.cur.execute("SELECT * FROM schedule WHERE title=?", (title,))
        rows = self.cur.fetchall()
        return rows

db_schedule = DB_schedule()
