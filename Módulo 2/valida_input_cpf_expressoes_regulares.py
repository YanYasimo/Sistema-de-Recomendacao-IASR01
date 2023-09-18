#Valida input CPF

import re

padrao_cpf = re.compile(r"(\d{3}\.){2}\d{3}-\d{2}|(\d{11})")

cpf1 = "123.456.789-00"
cpf2 = "12345678900"

if padrao_cpf.fullmatch(cpf1):
    print(f"{cpf1} é um CPF válido")
else:
    print(f"{cpf1} é um CPF inválido")

if padrao_cpf.fullmatch(cpf2):
    print(f"{cpf2} é um CPF válido")
else:
    print(f"{cpf2} é um CPF inválido")