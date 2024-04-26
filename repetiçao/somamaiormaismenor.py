valor = int(input())

maior = None
menor = None

for i in range(10):

    if maior is None or valor > maior:
        maior = valor

    if menor is None or valor < menor:
        menor = valor

soma = maior + menor
print(soma)
