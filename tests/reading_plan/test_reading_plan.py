from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest


expected = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Não deixe para depois: Python...",
                    4,
                ),
                (
                    "Selenium, BeautifulSoup ou Parsel?...",
                    3,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Pytest + Faker: a combinação poderosa dos testes!",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("FastAPI e Flask: frameworks para APIs em Python", 15),
        ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
    ],
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    result = ReadingPlanService.group_news_for_available_time(10)
    assert result == expected
