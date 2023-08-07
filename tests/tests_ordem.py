import unittest
from unittest.mock import patch
import random
from main import main
from models.ordem import Ordem
import yfinance as yf


class TestStringMethods(unittest.TestCase):

    def test_ordem(self):

        lista_acoes = ['AGRO3.SA', 'VIVT3.SA', 'RANI3.SA', 'SAPR11.SA', 'ITSA4.SA', 'TAEE11.SA']
        lista_cpf = ['405.880.370-36', '476.085.220-46', '312.560.510-55', '673.927.414-20', '348.877.924-68', '992.310.922-43', '097.313.249-33']
        acao = lista_acoes[random.randint(0, len(lista_acoes) - 1)]
        cpf = lista_cpf[random.randint(0, len(lista_cpf) - 1)]

        inputs = ["2", cpf, acao, 1, 'n']

        with patch("builtins.input", side_effect=inputs):
            main()

        info = yf.Ticker(acao).info
        ordem_esperada = f"('{info['longName']}', '{info['symbol']}', Decimal('{info['currentPrice']}'), Decimal('1'))"

        ordem = Ordem()
        ordem_inserida = ordem.select_ordem(cpf)
        ultima_ordem = ordem_inserida[len(ordem_inserida) - 1]
        ordem_comparacao = f"{ultima_ordem[1], ultima_ordem[2], ultima_ordem[3], ultima_ordem[4]}"

        self.assertIn(ordem_esperada, ordem_comparacao)

