import unittest
from faker import Factory
from utils.cpf import gerar_cpf
from unittest.mock import patch

from main import main, clientes


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Factory.create('pt_BR')
        return fake.name();

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gerar_cpf()
        inputs = ["1", nome, cpf, "27.161.525-4", "01/01/2000", "54762620", "700", "não"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "27.161.525-4",
            "data_nascimento": "01/01/2000",
            "endereco":{"CEP": "54762-620", "Logradouro": "Rua Pio XII","Complemento": "", "Bairro": "Bairro Novo do Carmelo", "Cidade": "Camaragibe", "Estado": "PE"},
            "numero_casa": "700"
        }

        self.assertIn(cliente_esperado, clientes)
