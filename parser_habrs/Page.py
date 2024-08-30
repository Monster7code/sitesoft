class Page:
    link_articles = "Сслылка на статьи контейнера"
    name = "Название хабра"

    def __init__(self, name_habr):
        if name_habr == "Хабр":
            self.link_articles = "https://habr.com/ru/feed/"
            self.name = name_habr
        elif name_habr == "Пикабу":

            self.link_articles = "https://pikabu.ru/"
            self.name = name_habr



