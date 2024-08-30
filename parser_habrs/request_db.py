import requests
from datetime import datetime


def get_habrs():
    request = requests.get(url="http://127.0.0.1:8000/get_habr")

    return request.json().get("name_habr")


async def check_on_article(link):

    request = requests.post(url="http://127.0.0.1:8000/check_link", json={"link": link})
    status = request.json().get("status")
    return status


async def set_article_on_db(link_article, link_user, time_public, header, habr):
    # Убираю лишнее из даты
    date_object = datetime.strptime(time_public, "%Y-%m-%d, %H:%M")
    # Обратно в строку
    date_string = date_object.strftime("%Y-%m-%d %H:%M:%S")

    json = {
        "article_link": link_article,
        "author_link": link_user,
        "date_of_publication":  date_string,
        "header": header,
        "resource": habr,
    }
    request = requests.post(url="http://127.0.0.1:8000/set_article_on_db", json=json)
    status = request.json().get("status")
    return status
