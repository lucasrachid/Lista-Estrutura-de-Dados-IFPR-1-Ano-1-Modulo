produto = input('Qual o nome do produto que você precisa ? ').strip()
desconto = float(input("Quantos " '%' " de desconto ? ").strip())
descontoPorcentagem = desconto / 100
valorProduto = float(input('Qual o valor do produto ? ').strip())
print(30 * '-')
print(f'Produto: {produto}')
print(30 * '-')
print(
    f'Valor: R$ {valorProduto}\nDesconto: R$ {valorProduto * descontoPorcentagem}')
print(30 * '-')
print(f'Valor final: R$ {valorProduto - (valorProduto * descontoPorcentagem)}')
print(30 * '-')
