valorHora = float(input('Quanto voce ganha por hora ? '))
horasTrabalhadas = float(input('Quantas horas voce trabalha por dia ? '))
print(
    f'Voce irá receber {valorHora * horasTrabalhadas} reais ao dia, considerando que em um mes de 30 dias, voce trabalhou \ntodos os 30 dias, irá receber {(valorHora * horasTrabalhadas) * 30} reais no mês')
