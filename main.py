"""Neste módulo, há apenas duas funcões:  a que cria o menu e a main(), que é a função pela qual
o sistema começa rodar."""

from DAO import Dao

dao_class_object = Dao()

def menu ():
    print("")
    print("AQUI É O MENU".center(110))
    list_menu_itens = ["Sair", "Ver carros ", "Adicionar carro ", "Editar um carro",
                        "Excluir carro"]

    for number, item in enumerate(list_menu_itens):
        print(f'Nº  {number } '.rjust(50), f'--->  "{item}"')

    menu_options = int(input("\nDigite o número da opção a ser usada:  ".upper()) )

    return menu_options

def main():
    while True:
        op_menu = menu()

        if op_menu == 1:
            search_possibilities = ['MARCA (digitando o nome da marca).',
                                    'ANO DE LANÇAMENTO (digite o ano para ver a lista de veículos)', ''
                                    'PREÇO MÁXIMO (informe um valor e aparecerão carros com preços iguais ou '
                                                                                                     'menores do que o valor passado).']

            print("\nPesquise por: ")
            for count, item in enumerate(search_possibilities):
                print(f'Nº  {count+1} '.rjust(40), f'--->  "{item}"')

            search_criteria = (input("\nFaça aqui a sua pesquisa: ".upper()))

            dao_class_object.see_cars(search_criteria)
        elif op_menu == 2:
            dao_class_object.add_car()

        elif op_menu == 3:
            pass
        elif op_menu == 4:
            pass
        elif op_menu == 0:
            print("Encerrando o programa...".upper())
            break
        else:
            print("Você digitou algo inválido. Leia o menu e escolha uma das opcões\n.". upper())

if __name__ == "__main__":
    main()