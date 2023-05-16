from tech_news.database import search_news
import re
from datetime import datetime

# Requisito 7


def search_by_title(title):
    filtered = []
    result = search_news({"title": re.compile(title, re.IGNORECASE)})
    for news in result:
        filtered.append((news["title"], news["url"]))
    return filtered


# Requisito 8
def search_by_date(date):
    # if not datetime.fromisoformat(date):
    #     raise ValueError()
    valid_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    filtered = [
        (news["title"], news["url"])
        for news in search_news({"timestamp": valid_date})
    ]
    return filtered


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# print(search_by_title("site responsivo:"))
# print(search_by_date("2023-05-10"))
