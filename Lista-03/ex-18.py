valorProduto = float(
    input('Qual o valor do produto que está adquirindo ? ').strip())
if (valorProduto > 100):
    desconto = valorProduto - (valorProduto * 0.10)
    print(
        f'O seu produto custa {valorProduto}, com 10% de desconto ele irá sair por {desconto}')
elif (valorProduto > 0 and valorProduto <= 100):
    print('Infelizmente o valor da sua compra não alcançou limite minimo para promoção.')
else:
    print('Valor inválido.')
