numero = int(input('Diga um numero inteiro: ').strip())
if (numero > 0):
    if (numero % 2 == 0):
        print(f'O numero {numero} é par.')
elif (numero < 0):
    print(f'O número é {numero}, somado 100 fica {numero + 100}')
else:
    print('Dado inválido.')
