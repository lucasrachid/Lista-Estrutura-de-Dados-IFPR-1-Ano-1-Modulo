idadeUsuario = int(input('Qual a sua idade ? ').strip())
if (idadeUsuario >= 18):
    salario = float(input('Qual o seu salário ? ').strip())
    reajuste = salario * 1.05
    print(
        f'O seu salário é {salario:.2f} reais, com reajuste de 5% vai para {reajuste:.2f} reais')
elif (idadeUsuario > 0 and idadeUsuario < 18):
    print('Cálculo não permitido.')
else:
    print('Idade inválida.')
