import unittest
from faker import Factory
from utils.cpf import gerar_cpf
from unittest.mock import patch

from main import main
from models.cliente import Cliente
from models.endereco import Endereco


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Factory.create('pt_BR')
        return fake.name()

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gerar_cpf()
        inputs = ["1", '1', nome, cpf, "12.345.657-4", "01/01/2000", "59067310", "12", "não"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente = Cliente()
        cliente_esperado = f"('{nome}', '{cpf}', '12.345.657-4', datetime.date(2000, 1, 1))"

        cliente_inserido = cliente.select_cliente_cpf(cpf)
        comparar_cliente = f"{cliente_inserido[0][1:len(cliente_inserido[0])]}"

        self.assertIn(cliente_esperado, comparar_cliente)

              #  "('Isabelly da Mata', '979.407.927-84', '27.161.525-4', datetime.date(2000, 1, 1))"
              #  "('Isabelly Da Mata', '979.407.927-84', '27.161.525-4', datetime.date(2000, 1, 1))"
