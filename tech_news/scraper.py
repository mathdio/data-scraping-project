import requests
from parsel import Selector
import time

# Requisito 1


def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2


def scrape_updates(html_content):
    news_list = []
    selector = Selector(text=html_content)

    for link in selector.css(".cs-overlay-link::attr(href)").getall():
        news_list.append(link)
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
