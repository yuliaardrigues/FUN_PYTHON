import time

def descobrir_interruptores(numero_interruptores, numero_lampadas):
    interruptores = [False] * numero_interruptores
    mapa_interruptores = {}

    # Primeira ida à sala das lâmpadas
    for i in range(numero_interruptores):
        interruptores[i] = True
        time.sleep(1)
        interruptores[i] = False

    # Segunda ida à sala das lâmpadas
    for i in range(numero_interruptores):
        interruptores[i] = True
        time.sleep(1)

    for i in range(numero_interruptores):
        interruptores[i] = False

    # Mapeando os interruptores às lâmpadas com base na temperatura simulada
    for i in range(numero_lampadas):
        if temperatura_lampada(i) > 15:  # Suponha que uma temperatura superior a 15 indica que a lâmpada está acesa
            mapa_interruptores[i+1] = i

    return mapa_interruptores

# Função para simular a temperatura de uma lâmpada
def temperatura_lampada(numero_lampada):
    if numero_lampada == 0:
        return 30  # Lâmpada 1 está quente
    elif numero_lampada == 1:
        return 20  # Lâmpada 2 está fria
    else:
        return 10  # Lâmpada 3 está fria

# Testando a função
numero_interruptores = 3
numero_lampadas = 3

mapa_interruptores = descobrir_interruptores(numero_interruptores, numero_lampadas)

print(f"Mapa de interruptores para lâmpadas: {mapa_interruptores}")
