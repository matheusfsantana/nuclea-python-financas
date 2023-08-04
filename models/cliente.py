from repository.database import Database
from utils.cpf import validar_cpf
from utils.rg import validar_rg
from utils.data_nascimento import valida_data
from models.endereco import Endereco


class Cliente:
    def __init__(self):
        self.table = "cliente"
        self.table_attributes = "nome, cpf, rg, data_nascimento"
        self.params = "%s, %s, %s, %s"

        self.nome = None
        self.cpf = None
        self.rg = None
        self.data_nascimento = None

        self.database = Database()

    def add_cliente(self):
        self.nome = input("Nome: ").title()
        self.cpf = validar_cpf(input("CPF: "))
        self.rg = validar_rg(input("RG: "))
        self.data_nascimento = valida_data()

        values = (self.nome, self.cpf, self.rg, self.data_nascimento)

        cliente = self.database.insert(self.table, self.table_attributes, self.params, values)

        if cliente is None:
            print("Cliente já existe!")
        else:
            endereco = Endereco()
            cliente_endereco = endereco.add_endereco(cliente[0])
            print("Cliente cadastrado com sucesso!")
            print(cliente[1:len(cliente)])
            print(cliente_endereco[1:len(cliente_endereco)-1])

    def select_cliente_cpf(self, cpf):

        condition = f"cpf = '{cpf}'"
        select = self.database.select(self.table, condition)
        if select is not None:
            return select


    def update_cliente(self):
        cpf = validar_cpf(input("Digite o CPF do cliente: "))
        cliente = self.select_cliente_cpf(cpf)
        if cliente is not None:
            self.nome = input("Nome: ").title()
            self.cpf = validar_cpf(input("CPF: "))
            self.rg = validar_rg(input("RG: "))
            self.data_nascimento = valida_data()

            set_update = f"nome='{self.nome}', cpf='{self.cpf}', rg='{self.rg}', data_nascimento='{self.data_nascimento}'"
            condition = f"cpf = '{cliente[0][2]}'"

            cliente_atualizado = self.database.update(self.table, set_update, condition)

            if cliente_atualizado is not None:
                print("Cliente atualizado: ")
                print(cliente_atualizado)

    def delete_cliente(self):
        cliente = self.select_cliente_cpf()
        if cliente is not None:
            condition = f"cpf = '{cliente[0][2]}'"
            result = self.database.delete(self.table, condition)
            print("Cliente deletado com sucesso!")

