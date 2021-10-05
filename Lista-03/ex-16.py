numero = int(input('Diga um valor inteiro positivo: ').strip())
while (numero < 0):
    print(f'O numero {numero} é negativo, por favor, tente novamente')
    numero = int(input('Diga um valor inteiro positivo: ').strip())
if (numero > 0):
    print(f'O numero é {numero}, a multiplicacao dele por 10 é {numero * 10}')
