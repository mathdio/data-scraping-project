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
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next.page-numbers::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    news_info = {}
    selector = Selector(text=html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    news_info["url"] = url

    title = selector.css("h1.entry-title::text").get()
    news_info["title"] = title.strip()

    timestamp = selector.css(".meta-date::text").get()
    news_info["timestamp"] = timestamp

    writer = selector.css(".author a::text").get()
    news_info["writer"] = writer

    reading_time = selector.css(".meta-reading-time::text").re_first(r"\d+")
    news_info["reading_time"] = int(reading_time)

    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    news_info["summary"] = "".join(summary).strip()

    category = selector.css(".label::text").get()
    news_info["category"] = category
    return news_info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


html = fetch(
    "https://blog.betrybe.com/carreira/empowerment-lideranca-o-que-e/"
)
print(scrape_news(html))
