salarioMinimo = 1039
salarioUsuario = float(input('Qual o valor do seu salário ? ').strip())
salariosRecebido = salarioUsuario / salarioMinimo
valorAjuste = salarioMinimo - salarioUsuario
if (salarioUsuario >= 1039):
    print(
        f'O seu salário é {salarioUsuario:.2f} reais, equivale a {salariosRecebido:.2f} salários minimos')
elif (salarioUsuario > 0 and salarioUsuario < 1039):
    print(
        f'O seu salário é {salarioUsuario:.2f} reais, não chega a 1 salário minimo vigente.')
else:
    print('Não é um valor válido')
