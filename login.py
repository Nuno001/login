nome = input("Qual seu nome")
senha = input("Qual sua senha")

senha_bd("Peste")
nome_bd("Luiz")


if nome_bd == nome and senha_bd == senha:
    print(f'{nome} é maior de idade.')
else:
    print('usuario n encontrado')
