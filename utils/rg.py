import re


def validate_rg(rg):
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    if re.match(padrao_rg, rg):
        return True
    else:
        return False


def validar_rg(rg):
    while not validate_rg(rg):
        rg = input("Digite um RG válido: ");

    return rg;
