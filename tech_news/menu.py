from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
import sys

# Requisitos 11 e 12


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )
    features = {
        "0": "Digite quantas notícias serão buscadas: ",
        "1": "Digite o título: ",
        "2": "Digite a data normato aaaa-mm-dd: ",
        "3": "Digite a categoria: ",
    }

    if option in ["0", "1", "2", "3"]:
        entry = input(features[option])
        features_functions(option, entry)

    elif option == "4":
        print(top_5_categories())
    elif option == "5":
        print("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")


def features_functions(option, entry):
    if option == "0":
        print(get_tech_news(int(entry)))
    elif option == "1":
        print(search_by_title(entry))
    elif option == "2":
        print(search_by_date(entry))
    elif option == "3":
        print(search_by_category(entry))
