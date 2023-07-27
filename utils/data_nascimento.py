from datetime import datetime


def valida_data():
    while True:
        data_nascimento = input("Data nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date();

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")

        except ValueError:
            print("Digite uma data válida");
