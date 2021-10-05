a = float(input('Diga um valor para A: ').strip())
b = float(input('Diga um valor para B: ').strip())
c = float(input('Diga um valor para C: ').strip())
if (a > b and a > c):
    print(f'O valor de A é {a} e é superior aos demais valores.')
elif (b > a and b > c):
    print(f'O valor de B é {b} e é superior aos demais valores.')
elif (c > a and c > b):
    print(f'O valor de C é {c} e é superior aos demais valores.')
else:
    print('Opção inválida.')
