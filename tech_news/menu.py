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

    if option in ["0", "1", "2", "3"]:
        features = {
            "0": "Digite quantas notícias serão buscadas: ",
            "1": "Digite o título: ",
            "2": "Digite a data normato aaaa-mm-dd: ",
            "3": "Digite a categoria: ",
        }
        input(features[option])

    if option == "4":
        pass
    elif option == "5":
        exit()
    else:
        print("Opção inválida")
