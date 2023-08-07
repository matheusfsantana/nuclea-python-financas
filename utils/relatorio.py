import yfinance as yf


def obter_dados_acao(ticker, nome_arquivo):
    try:
        acao = yf.download(ticker, start='2020-01-01', end='2023-01-01')

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatorio da ação: " + ticker + "\n")
            arquivo.write(str(acao.tail()))

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")



