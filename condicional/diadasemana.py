num = int(input("Digite um número de 1 a 7: "))

dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if 1 >= num <= 7:
    print(dias_da_semana[num])
else:
    print("Número inválido.")