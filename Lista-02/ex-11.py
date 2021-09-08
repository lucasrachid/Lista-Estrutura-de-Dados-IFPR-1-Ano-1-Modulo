a = float(input('Diga um valor para A '))
b = float(input('Diga um valor para B '))
c = float(input('Diga um valor para C '))

equacao = (b ** 2) - 4 * a * c

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif equacao < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + equacao ** (1 / 2)) / (2 * a)
    x2 = (-b - equacao ** (1 / 2)) / (2 * a)

    print(f"x1: {x1}, x2: {x2}")
