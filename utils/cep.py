import requests as rq


def busca_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = rq.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            endereco = {
                "CEP": dados['cep'],
                "Logradouro": dados['logradouro'],
                "Complemento": dados['complemento'],
                "Bairro": dados['bairro'],
                "Cidade": dados['localidade'],
                "Estado": dados['uf']
            }
            return endereco
        else:
            print("CEP Inválido ou não encontrado.")


def valida_cep():
    while True:
        cep_input = input("CEP: ")

        if cep_input.isdigit() and len(cep_input) == 8:
            return busca_cep(cep_input)
