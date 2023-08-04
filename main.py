from utils.menus import *


def main():

    validador = True
    while validador:
        op = menu_principal()
        if op == 1:
            sub_menu_cliente()
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            break
        else:
            print("Opção inválida!")

        validador = retorna_menu()


if __name__ == "__main__":
    main()
