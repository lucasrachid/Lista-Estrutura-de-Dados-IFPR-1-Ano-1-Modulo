n1 = float(input('Diga a nota da sua primeira prova: ').strip())
n2 = float(input('Diga a nota da sua segunda prova: ').strip())
media = (n1 + n2) / 2
if (media > 0 and media < 60):
    print('Reprovado')
elif (media > 60 and media <= 100):
    print('Aprovado')
else:
    print('Não é um valor válido')
