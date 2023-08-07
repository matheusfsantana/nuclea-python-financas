import datetime
from utils.cpf import validar_cpf
from utils.ticker import validar_ticker
from repository.database import Database
from models.cliente import Cliente
from utils.analise_carteira import analisar_carteira
from utils.relatorio import obter_dados_acao


class Ordem:
    def __init__(self):
        self.table = "ordem"
        self.table_attributes = "nome, ticker, valor_compra, quantidade_compra, data_compra, cliente_id"
        self.params = "%s, %s, %s, %s, %s, %s"

        self.id = None
        self.nome = None
        self.ticker = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None

        self.database = Database()

    def cadastrar_ordem(self):
        cliente = Cliente()
        print("Informe seu CPF para cadastrar uma nova ordem/ação")
        cpf = validar_cpf(input("CPF: "))
        cliente_selecionado = cliente.select_cliente_cpf(cpf)

        if cliente_selecionado is not None:
            self.cliente_id = cliente_selecionado[0][0]
            ticker_info = validar_ticker()
            print(ticker_info)
            if '.SA' in ticker_info['symbol']:
                self.ticker = ticker_info['symbol']
            else:
                self.ticker = ticker_info['symbol'] + '.SA'

            if 'longName' not in ticker_info:
                self.nome = input("Digite o nome da empresa: ")
            else:
                self.nome = ticker_info['longName']

            print(self.nome)

            if 'currentPrice' not in ticker_info:
                self.valor_compra = float(input("Digite o valor da ação: "))
            else:
                self.valor_compra = ticker_info['currentPrice']

            self.quantidade_compra = int(input(f"Valor da ação: {self.valor_compra}\nDigite a quantidade de compra: "))
            self.data_compra = datetime.datetime.now().date()

            values = (self.nome, self.ticker, self.valor_compra, self.quantidade_compra, self.data_compra, self.cliente_id)

            resultado = self.database.insert(self.table, self.table_attributes, self.params, values)
            print(f"Ação cadastrada com sucesso para o cliente {cpf}!")
            print(resultado)

        else:
            print("Cliente não encontrado!")

    def obter_relatorio_cliente(self):
        cpf = validar_cpf(input("Para obter o seu relátorio das ações, digite seu CPF: "))
        tickers = ""
        # nome do arquivo = relatorio_idcliente_cpf

        results = self.select_ordem(cpf)
        nome_arquivo = f"relatorio_{results[0][0]}_{cpf}"

        if results is not None:
            for i in range(0, len(results)):
                # [:-3] para remover o .SA pois estava dando conflito no download
                tickers += f"{results[i][2][:-3]} "
            obter_dados_acao(tickers, nome_arquivo)

    def analisar_carteira_cliente(self):
        cpf = validar_cpf(input("Para obter a análise das suas ações digite seu CPF: "))

        tickers = []

        results = self.select_ordem(cpf)
        if results is not None:
            for i in range(0, len(results)):
                # [:-3] para remover o .SA pois estava dando conflito no download
                tickers.append(results[i][2][:-3])

            analisar_carteira(tickers)

    def select_ordem(self, cpf):
        cliente = Cliente()
        cliente_selecionado = cliente.select_cliente_cpf(cpf)

        if cliente_selecionado is not None:
            condition = f"""
                cliente_id = (SELECT id FROM cliente WHERE cpf = '{cpf}')
            """

            results = self.database.select(self.table, condition)
            if results is not None:
                return results
            else:
                print("Nenhuma ação cadastrada")
        else:
            print("Cliente não encontrado!")
