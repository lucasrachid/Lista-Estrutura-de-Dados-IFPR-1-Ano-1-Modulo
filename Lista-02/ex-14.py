valorHora = float(input('Quanto voce ganha por hora ? '))
qtdHoras = float(input(
    'Quantas horas voce trabalhou no mês ? '))
salarioBruto = valorHora * qtdHoras
irrf = salarioBruto * 0.075
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.01
salarioLiquido = salarioBruto - irrf - inss - sindicato
print(12 * '-' + ' Holerite ' + 12 * '-')
print(f'+ Salário Bruto: R$ {salarioBruto:.2f} reais')
print(f'- IR (7.5%): R$ {irrf:.2f} reais')
print(f'- INSS (8%): R$ {inss:.2f} reais')
print(f'- Sindicato (1%): R$ {sindicato:.2f} reais')
print(f'= Salário Líquido: R$ {salarioLiquido} reais')
print(34 * '-')
