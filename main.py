from utils.menus import *
from models.ordem import Ordem


def main():

    validador = True
    while validador:
        op = menu_principal()
        if op == 1:
            sub_menu_cliente()
        elif op == 2:
            ordem = Ordem()
            ordem.cadastrar_ordem()
        elif op == 3:
            ordem = Ordem()
            ordem.analisar_carteira_cliente()
        elif op == 4:
            ordem = Ordem()
            ordem.obter_relatorio_cliente()
        elif op == 5:
            break
        else:
            print("Opção inválida!")

        validador = retorna_menu()


if __name__ == "__main__":
    main()
