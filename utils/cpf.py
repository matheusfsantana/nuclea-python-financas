from validate_docbr import CPF


def validar_cpf(cpf):
    validar = CPF()

    while not validar.validate(cpf):
        cpf = input("CPF inválido, digite novamente: ")

    if len(cpf) > 11:
        return cpf
    else:
        return validar.mask(cpf)


def gerar_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate(True)
    return cpf_gerado;

