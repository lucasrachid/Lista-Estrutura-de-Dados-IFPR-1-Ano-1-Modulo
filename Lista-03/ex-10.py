n1 = int(input('Diga um número inteiro, entre 0 e 100: ').strip())
if (n1 >= 0 and n1 <= 100):
    print(f'O seu numero é {n1}, número no intervalo definido.')
else:
    print('Número fora do intervalo!')
