from math import ceil
metros = float(
    input('Quantos metros quadrados tem a parede a ser pintada ? ').strip())
conversao = metros / 3.0
custoLata = 120
custoTotal = conversao * custoLata
print(f'Voce irá precisar de {conversao:.2f} litros de tinta.')
if conversao > 0.0 and conversao <= 18.0:
    print(
        f'Será necessário apenas 1 Lata de tinta, custando R${custoLata} reais.')
elif conversao > 18:
    conversao2 = ceil(conversao / 18)
    print(
        f'Será necessário {conversao2} Latas de tinta, custando no total R$ {conversao2 * custoLata} reais.')
else:
    print('Dado inválido.')
