from tech_news.database import find_news
from collections import Counter

# Requisito 10


def top_5_categories():
    db_result = find_news()
    categories_filter = [result["category"] for result in db_result]
    counter = Counter(categories_filter).most_common()
    values_set = set(frequency[1] for frequency in counter)
    values_list = [value for value in values_set]
    values_list.sort(reverse=True)
    sorted_categories = []
    for value in values_list:
        same_frequency = [
            category[0] for category in counter if category[1] == value
        ]
        same_frequency.sort()
        sorted_categories.extend(same_frequency)
    return sorted_categories[:5]
