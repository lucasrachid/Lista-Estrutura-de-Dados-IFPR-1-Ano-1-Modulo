# Questao 10
# print('=' * 12 + ' Produtos ' + '=' * 12)
# print('1 - Alimento não Perecível')
# print('2 - 2, 3 ou 4 - Alimento Perecível')
# print('5 ou 6 - Vestuário')
# print('7 - Higiene Pessoal')
# print('8, 9, 10 - Utensílios domésticos')
# print('=' * 34)
# n1 = int(input('Digite o número do produto: ').strip())
# if (n1 == 1):
#     print('Você escolheu Alimentos não perecíveis.')
# elif (n1 == 2 or n1 == 3 or n1 == 4):
#     print('Você escolheu Alimentos perecíveis.')
# elif (n1 == 5 or n1 == 6):
#     print('Você escolheu Vestuário.')
# elif (n1 == 7):
#     print('Você escolheu produtos de Higiene pessoal.')
# elif (n1 == 8 or n1 == 9 or n1 == 10):
#     print('Você escolheu Utensílios domésticos.')
# else:
#     print('Código inválido.')

# Questao 09
# cachorroQuente = 100
# bauruSimples = 101
# bauruComOvo = 102
# hamburguer = 103
# cheeseBurguer = 104
# refrigerante = 105
# valorCachorroQuente = 1.20
# valorBauruSimples = 1.30
# valorBauruComOvo = 1.50
# valorHamburguer = 1.20
# valorCheeseBurguer = 1.30
# valorRefrigerante = 1.00
# print('Bem vindo a lanchonete X - Infarto')
# opcoes = int(input('Digite 1 para ver o cardápio e 2 para sair: ').strip())
# if (opcoes == 1):
#     print('==' * 10 + ' Cardápio ' + 10 * '==')
#     print('Cachorro quente - Cod 100 - Valor 1,20')
#     print('Bauru Simples - Cod 101 - Valor 1,30')
#     print('Bauru com Ovo - Cod 102 - Valor 1,50')
#     print('Hamburguer - Cod 103 - Valor 1,20')
#     print('CheeseBurguer - Cod 104 - Valor 1,30')
#     print('Refrigerante - Cod 105 - Valor 1,0')
#     print('==' * 25)
#     pedido = int(input('Digite o código do item do pedido: ').strip())
#     if (pedido == cachorroQuente):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorCachorroQuente
#         print(
#             f'Ok, o pedido é referente a {quantidade} Cachorro quente, totalizando R${valorPedido:.2f} reais.')
#     elif (pedido == bauruSimples):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorBauruSimples
#         print(
#             f'Ok, o pedido é referente a {quantidade} Bauru simples, totalizando R${valorPedido:.2f} reais.')
#     elif (pedido == bauruComOvo):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorBauruComOvo
#         print(
#             f'Ok, o pedido é referente a {quantidade} Bauru com Ovo, totalizando R${valorPedido:.2f} reais.')
#     elif (pedido == hamburguer):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorHamburguer
#         print(
#             f'Ok, o pedido é referente a {quantidade} Hamburguer, totalizando R${valorPedido:.2f} reais.')
#     elif (pedido == cheeseBurguer):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorCheeseBurguer
#         print(
#             f'Ok, o pedido é referente a {quantidade} CheeseBurguer, totalizando R${valorPedido:.2f} reais.')
#     elif (pedido == refrigerante):
#         quantidade = int(input('Qual a quantidade ? '))
#         valorPedido = quantidade * valorRefrigerante
#         print(
#             f'Ok, o pedido é referente a {quantidade} Refrigerante, totalizando R${valorPedido:.2f} reais.')
#     else:
#         print('Opção inválida.')
# elif (opcoes == 2):
#     print('Tudo bem, até uma próxima!')
# else:
#     print('Opção inválida.')

# Questao 06
# n1 = int(input('Digite um numero: ').strip())
# if (n1 >= 0):
#     if (n1 % 2 == 0):
#         print(f'O número {n1} é positivo e Par.')
#     elif (n1 % 3 == 0):
#         print(f'O número {n1} é positivo, Ímpar, múltiplo de 3.')
#     else:
#         print(f'O número {n1} é Positivo e ímpar.')
# elif (n1 < 0):
#     conversao = n1 * -1
#     if (conversao % 2 == 0):
#         print(f'O número {n1} é Negativo e Par.')
#     elif (conversao % 3 == 0):
#         print(f'O número {n1} é Negativo, Ímpar, múltiplo de 3.')
#     else:
#         print(f'O número {n1} é Negativo e ímpar.')

# Questao 08
# idade = int(input('Qual a idade do nadador ? ').strip())
# if (idade > 18):
#     print('O nadador está classificado na categoria adulto.')
# elif (idade >= 14 and idade <= 18):
#     print('O nadador está classificado na categoria Juvenil B.')
# elif (idade >= 11 and idade <= 13):
#     print('O nadador está classificado na categoria Juvenil A.')
# elif (idade >= 8 and idade <= 10):
#     print('O nadador está classificado na categoria Infantil B.')
# elif (idade >= 5 and idade <= 7):
#     print('O nadador está classificado na categoria Infantil A.')
# else:
#     print('Idade inválida.')

# Questao 07
from random import randint
import math
from time import sleep
from typing import Match
print('==' * 30)
print('1 - Calcular a soma de 3 números.')
print('2 - Calcular a raiz quadrada de um número.')
print('3 - Calcular a potência de um número.')
print('4 - Calcular o valor de uma fórmula matemática.')
print('5 - Exibir na tela um número aleatório entre 1 e 100.')
print('==' * 30)
opcao = int(input('Escolha uma das opções acima: ').strip())
print('==' * 30)
if (opcao == 1):
    n1 = float(input('Diga um valor para o número 01: ').strip())
    n2 = float(input('Diga um valor para o número 02: ').strip())
    n3 = float(input('Diga um valor para o número 03: ').strip())
    soma = n1 + n2 + n3
    print(f'A soma dos números {n1}, {n2} e {n3} totaliza {soma:.2f}')
elif (opcao == 2):
    n1 = float(
        input('Diga o valor do número que você deseja a Raiz Quadrada: ').strip())
    raiz = math.sqrt(n1)
    print(f'A Raiz Quadrada do número {n1} é {raiz:.2f}')
elif (opcao == 3):
    n1 = int(input('Digite um valor para a Base: ').strip())
    n2 = int(input('Digite um valor para o Expoente: ').strip())
    potencia = math.pow(n1, n2)
    print(f'A potência é {potencia}')
elif (opcao == 4):
    n1 = int(input('Diga o valor para N1: ').strip())
    n2 = int(input('Diga o valor para N2: ').strip())
    formula = (n1 ** 3) + math.sin(n2) / math.sqrt((n1 / 2) + (n2 ** 4) + 1)
    print(f'O resultado da fórmula é {formula:.2f}')
elif (opcao == 5):
    print('Gerando número aleatório...')
    sleep(1)
    print('Só um momento...')
    sleep(1)
    print(f'O número gerado é {randint(1, 100)}')
else:
    print('Opcao inválida.')
