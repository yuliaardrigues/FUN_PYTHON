def inverter_string(string):
    # Usando a técnica de slicing para inverter a string
    return string[::-1]

entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
