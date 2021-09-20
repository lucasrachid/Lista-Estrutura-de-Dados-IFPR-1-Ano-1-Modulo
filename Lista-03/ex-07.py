sexo = input(
    'Diga qual o seu sexo (M para Masculino, F para Feminino): ').strip().upper()
if (sexo == 'M'):
    print('Seu sexo é Masculino')
elif (sexo == 'F'):
    print('Seu sexo é Feminino')
else:
    print('Não é uma alternativa válida')
