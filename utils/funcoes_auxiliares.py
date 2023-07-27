def retorna_menu_principal():
    escolha = input("Deseja fazer outra operação? (sim / não)").lower()
    return escolha == "sim"


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado


