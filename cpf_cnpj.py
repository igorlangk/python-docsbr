from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def verifica_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")


class Cpf:
    def __init__(self, cpf):
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido!")

    def valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()


class Cnpj:
    def __init__(self, cnpj):
        if self.valida_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido!")

    def valida_cnpj(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()
