import re


class TelefoneBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número de telefone incorreto!")

    def __str__(self):
        if "None" in self.formata_telefone():
            telefone = self.formata_telefone().replace("None", "55")
            return telefone
        else:
            return self.formata_telefone()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        telefone_certo = re.search(padrao, telefone)
        if telefone_certo:
            return True
        else:
            return False

    def formata_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        telefone_certo = re.search(padrao, self.telefone)
        telefone = "+{}({}){}-{}".format(
            telefone_certo.group(1),
            telefone_certo.group(2),
            telefone_certo.group(3),
            telefone_certo.group(4)
        )
        return telefone
