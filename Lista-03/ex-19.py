salario = float(input('Qual o valor do seu salário ? ').strip())
if (salario == 1039):
    fgts = salario * 0.08
    inss = salario * 0.08
    salarioLiquido = salario - inss
    print(
        f'O seu salário Bruto é {salario}, com  é {salarioLiquido} reais, mais {fgts} reais de FGTS.')
elif (salario > 1039):
    fgts = salario * 0.08
    inss = salario * 0.08
    irrf = salario * 0.075
    salarioLiquido = salario - inss - irrf
    print(f'Seu salário liquido é {salarioLiquido} reais, ')
