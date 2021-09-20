idadeUsuario = int(input('Diga qual a sua idade: ').strip())
if (idadeUsuario >= 18):
    nome = input('Qual o seu nome ? ').strip()
    print(f'Bem vindo {nome}')
elif (idadeUsuario > 0 and idadeUsuario < 18):
    print('Entrada não permitida!')
else:
    print('Opcão inválida')
