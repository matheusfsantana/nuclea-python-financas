from models.cliente import Cliente
from models.ordem import Ordem
from utils.cpf import validar_cpf


def menu_principal():
    while True:
        try:
            print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea.")
            print("1 - Cliente\n"
                  "2 - Cadastrar ação\n"
                  "3 - Realizar análise da carteira\n"
                  "4 - Imprimir relatório da carteira\n"
                  "5 - Sair")

            op = int(input("Digite uma opção: "))
            return op
        except ValueError:
            print("Valor digitado inválido, digite um número inteiro!")


def sub_menu_cliente():
    while True:
        try:
            cliente = Cliente()
            print("Menu Cliente: ")
            print("1 - Cadastrar\n"
                  "2 - Consultar\n"
                  "3 - Atualizar\n"
                  "4 - Deletar")

            op = int(input("Digite uma opção: "))
            if op == 1:
                cliente.add_cliente()
            elif op == 2:
                cpf = validar_cpf(input("Digite o CPF do cliente: "))
                resultado = cliente.select_cliente_cpf(cpf)
                print(resultado)
            elif op == 3:
                cliente.update_cliente()
            elif op == 4:
                cliente.delete_cliente()
            else:
                print("Opção inválida!")
            break
        except ValueError:
            print("Valor digitado inválido, digite um número inteiro!")


def retorna_menu():
    escolha = input("Deseja fazer outra operação? (sim / não): ").lower()
    return escolha == "sim" or escolha == "s"


def sub_menu_ordem():
    pass
