import yfinance as yf


def validar_ticker():
    while True:
        try:
            ticker = input("Digite o ticker da ação: ").upper()
            info = yf.Ticker(ticker).info
            if info is not None:
                return info
        except Exception as e:
            print("Ticker inválido. Por favor, verifique e tente novamente.")
