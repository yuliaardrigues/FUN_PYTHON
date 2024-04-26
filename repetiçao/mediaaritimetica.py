soma = 0
contador = 0

for i in range(23, 484):
    if i % 2 == 0:
        soma += i
        contador += 1

media = soma / contador
print("A média aritmética dos números pares entre 23 e 483 é:", media)