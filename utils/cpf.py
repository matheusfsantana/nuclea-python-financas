from validate_docbr import CPF

def validar_cpf(cpf):
    validar = CPF()
    validar.mask(cpf)
    while not validar.validate(cpf):
        cpf = input("CPF inválido, digite novamente: ")
    return validar.mask(cpf)




