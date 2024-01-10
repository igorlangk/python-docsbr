from cpf_cnpj import Documento
from telefonebr import TelefoneBr
from data import DataBr
from cep import Cep

cpf = 44575438022
cnpj = 49486300000111
documento_um = Documento.verifica_documento(cnpj)
documento_dois = Documento.verifica_documento(cpf)

print(documento_um)
print(documento_dois)

telefone = "552733333333"
objeto_telefone = TelefoneBr(telefone)
print(objeto_telefone)

data_cadastro = DataBr()
print("Dia da semana: {} / Mês: {}".format(data_cadastro.semana_cadastro(), data_cadastro.mes_cadastro()))
print(data_cadastro)

cep = 29050902
objeto_cep = Cep(cep)
print(objeto_cep)

print(objeto_cep.acesso_via_cep())