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
    filtered = [
        (news["title"], news["url"])
        for news in search_news(
            {"category": re.compile(f"^{category}$", re.IGNORECASE)}
        )
    ]
    return filtered


print(search_by_category("erra"))
