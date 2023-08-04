from utils.cep import valida_cep
from repository.database import Database


class Endereco:
    def __init__(self):
        self.table = "endereco"
        self.table_attributes = "cep, logradouro, complemento, bairro, cidade, estado, numero_casa, cliente_id"
        self.params = "%s, %s, %s, %s, %s, %s, %s, %s"

        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.numero_casa = None
        self.cliente_id = None
        self.database = Database()

    def add_endereco(self, cliente_id):
        dados = valida_cep()
        self.cep = dados['CEP']
        self.logradouro = dados['Logradouro']
        self.complemento = dados['Complemento']
        self.bairro = dados['Bairro']
        self.cidade = dados['Cidade']
        self.estado = dados['Estado']
        self.numero_casa = int(input("Digite o numero da casa: "))
        self.cliente_id = cliente_id

        values = (self.cep, self.logradouro, self.complemento, self.bairro, self.cidade, self.estado, self.numero_casa, self.cliente_id)

        endereco = self.database.insert(self.table, self.table_attributes, self.params, values)
        return endereco
