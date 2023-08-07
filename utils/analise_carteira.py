import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def analisar_carteira(acoes):
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    df = pd.DataFrame()

    for i in acoes:
        cotacao = yf.download(i, start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()

