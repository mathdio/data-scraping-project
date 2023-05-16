from tech_news.database import search_news
import re

# Requisito 7


def search_by_title(title):
    filtered = []
    result = search_news({"title": re.compile(title, re.IGNORECASE)})
    for news in result:
        filtered.append((news["title"], news["url"]))
    return filtered


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# print(search_by_title("site responsivo:"))
