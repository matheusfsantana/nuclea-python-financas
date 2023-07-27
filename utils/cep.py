import requests as rq

def busca_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = rq.get(url);
