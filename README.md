# Utilidades Python

Este projeto implementa utilidades relacionadas a documentos, telefones, datas e CEPs. Originalmente aprendido durante o curso "Aprenda a programar em Python com Orientação a Objetos" na plataforma Alura.

## cpf_cnpy.py

Este arquivo contém classes para validar e formatar CPFs e CNPJs.

## telefonebr.py

Este arquivo inclui uma classe para validar e formatar números de telefone brasileiros.

## data.py

Aqui, você encontrará uma classe que lida com datas, fornecendo métodos para obter o mês, dia da semana, formato de data e tempo desde o cadastro.

## cep.py

Este arquivo contém uma classe para validar e formatar CEPs, além de realizar consultas à API ViaCEP para obter informações adicionais sobre o CEP.

## Como usar

- Clone o repositório: git clone https://github.com/seu-usuario/nome-do-repositorio.git
- Instale as dependências: pip install validate_docbr requests
- Execute o script de teste: python teste.py

## Exemplos de Uso

```python
# Exemplo de uso para todas as classes:
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