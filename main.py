from utils.funcoes_auxiliares import formata_texto, retorna_menu_principal
from utils.cpf import validar_cpf
from utils.rg import validar_rg
from utils.data_nascimento import valida_data
from utils.cep import busca_cep

clientes = [];

def main():

    validador = True;
    while validador:
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea.")
        print("1 - Cadastrar Cliente\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair");

        op = int(input("Digite uma opção: "));

        if op == 1:
            cliente = {
                "nome": formata_texto(input("Nome: ")),
                "cpf": validar_cpf(input("CPF: ")),
                "rg": validar_rg(input("RG: ")),
                "data_nascimento": valida_data(),
                "endereco": busca_cep(input("Digite o CEP: ")),
                "numero_casa": input("Numero da casa: ")
            }
            clientes.append(cliente);
            print(clientes);

            validador = retorna_menu_principal();


if __name__ == "__main__":
    main()
