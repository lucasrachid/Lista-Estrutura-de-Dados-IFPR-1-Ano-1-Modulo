n1 = float(input('Diga um valor: '))
if n1 == 0:
    print('O zero, 0, não é um número positivo nem negativo, já que não é maior nem menor que si mesmo. Entretanto, pode ser representado com sinal mais ou menos, +0 ou −0, indistintamente, já que não causa nenhuma ambiguidade nas operações aritméticas.')
elif n1 > 0:
    print(f'{n1} é um valor positivo!')
else:
    print(f'{n1} é um valor negativo!')
