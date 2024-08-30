
from urllib.parse import urljoin, urlparse, urldefrag
import asyncio
import logging
from Page import *
from request_db import *

import aiohttp
from bs4 import BeautifulSoup


async def page_habr(habr):
    # Создание сессии
    async with (aiohttp.ClientSession() as session):

        response = await session.get(habr.link_articles)
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        if habr.name == "Хабр":
            articles_list = soup.find(class_='tm-articles-list')
            articles = articles_list.find_all("article", "tm-articles-list__item")

        elif habr.name == "Пикабу":

            articles_list = soup.find("div", 'stories-feed__container')

            articles = articles_list.find_all("article", "story")
        tasks = []
        for article in articles:
            tasks.append(process_article(article, habr, session))

        await asyncio.gather(*tasks)


async def process_article(article, habr, session):
    try:
        if habr.name == "Хабр":
            if (article.find("div", "publication-type-label_type-news")) or (
            article.find("div", "publication-type-label_type-post")):
                return
            # Проверка на существование ссылки
            link_block = article.find("a", "tm-article-snippet__readmore")
            link = f'https://habr.com{link_block.get("href")}'
        elif habr.name == "Пикабу":
            block_content = article.find("div", "story__main")
            link_block = block_content.find("h2", "story__title")
            link = link_block.find("a").get("href")

        # Проверка есть ли уже это запись
        if await check_on_article(link):
            header, link_user, time_public = await page_article(link, habr)
            if await set_article_on_db(link, link_user, time_public, header, habr.name):
                print("Запись успешно добавлена")
            else:

                print("При добавления записи произошла ошибка")
        else:

            print("Запись уже сущетсвует")

    except Exception as e:

        return


async def page_article(url, habr):
    async with (aiohttp.ClientSession() as session):

        response = await session.get(f"{url}")
        html = await response.text()
        article = BeautifulSoup(html, 'html.parser')
        if habr.name == "Хабр":
            mini_profile = article.find("div", "tm-article-snippet__meta-container").find("div", "tm-article-snippet__meta")

            link_user = mini_profile.find("a", "tm-user-info__userpic")

            header = article.find("h1", "tm-title_h1").find("span")
            header = header.text
            link = f'https://habr.com{link_user.get("href")}'
            time = mini_profile.find("span", "tm-article-datetime-published").find("time")
            time = time.get("title")

        elif habr.name == "Пикабу":
            header = article.find("h1", "story__title").find("span")

            mini_profile = article.find("div", "story__user-info")
            link_user = mini_profile.find("a", "story__user-link")
            link = link_user.get("href")
            time = mini_profile.find("time", "story__datetime")
            header = header.text
            time = time.get("datetime")

        return header, link, time


async def run_periodically(interval):
    while True:
        for habr in get_habrs():
            name_habr = habr.get("resource_link")
            await page_habr(Page(name_habr))

        await asyncio.sleep(interval)

asyncio.run(run_periodically(600))