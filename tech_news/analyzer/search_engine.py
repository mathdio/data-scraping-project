from tech_news.database import search_news
import re
from datetime import datetime

# Requisito 7


def search_by_title(title):
    filtered = [
        (news["title"], news["url"])
        for news in search_news({"title": re.compile(title, re.IGNORECASE)})
    ]
    return filtered


# Requisito 8
def search_by_date(date):
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        filtered = [
            (news["title"], news["url"])
            for news in search_news({"timestamp": valid_date})
        ]
        return filtered
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# print(search_by_title("site responsivo:"))
# print(search_by_date("2023-05-10"))

date = "2023-05-17"
valid_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
print(valid_date)
