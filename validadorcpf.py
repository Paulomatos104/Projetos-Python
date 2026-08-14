cpf = input("Digite o CPF: ")
remover_caracteres = cpf.replace(".", "").replace("-", "")
remover_verificador = remover_caracteres[:-2]

primeiro_digito = sum(int(remover_verificador[i]) * (10 - i) for i in range(9))
resto1 = primeiro_digito % 11
if resto1 < 2:
    digito1 = 0
else:
    digito1 = 11 - resto1

segundo_digito = sum(int(remover_verificador[i]) * (11 - i) for i in range(9)) + digito1 * 2
resto2 = segundo_digito % 11
if resto2 < 2:
    digito2 = 0
else:
    digito2 = 11 - resto2

if digito1 == int(remover_caracteres[-2]) and digito2 == int(remover_caracteres[-1]):
    print("CPF válido")
else:
    print("CPF inválido")



    