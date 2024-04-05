salario = float(input("Digite o salario: "))
prestacao = float(input("Digite o valor da prestaçao:"))

porcentagem = salario * 0.30

if prestacao > porcentagem: 
  print("Nao concebido, prestação maior que o permitido")

else:
  print("Concebido, dentro do limite")
