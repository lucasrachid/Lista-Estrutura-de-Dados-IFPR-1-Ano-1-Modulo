conceito = input(
    'Qual o seu conceito na disciplina X ? (A, B, C ou D) ').strip().upper()
if (conceito == 'A' or conceito == 'B' or conceito == 'C'):
    print('Aprovado')
elif (conceito == 'D'):
    print('Reprovado')
else:
    print('Não é um conceito válido.')
