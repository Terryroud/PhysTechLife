class Note():
    def __init__(self, title, article, date):
        self._title = title
        self._article = article
        self._date = date

    @property
    def title(self):
        return self._title

    @property
    def article(self):
        return self._article

    @property
    def date(self):
        return self._date

    @title.setter
    def title(self, new_title):
        if new_title != self._title:
            self._title = new_title
        return self._title

    @article.setter
    def article(self, new_article):
        if new_article != self._article:
            self._article = new_article
        return self._article
