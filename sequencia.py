def sequencia_a(n):
    return n + 1

# Sequência b) 2, 4, 8, 16, 32, 64, ___
def sequencia_b(n):
    return 64 * 2

# Sequência c) 0, 1, 4, 9, 16, 25, 36, ___
def sequencia_c(n):
    return pow(7, 2)

# Sequência d) 4, 16, 36, 64, ___
def sequencia_d(n):
    return (8) ** 2

# Sequência e) 1, 1, 2, 3, 5, 8, ___
def sequencia_e(n):
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
n = 6  
proximo_numero = sequencia_e(n)
# Sequência f) 2,10, 12, 16, 17, 18, 19, ___
def sequencia_f(n):
    return n + 18


def proximo_elemento(sequencia, ultimo_elemento):
    return sequencia(ultimo_elemento + 1)


print("Sequência a):", proximo_elemento(sequencia_a, 7))
print("Sequência b):", proximo_elemento(sequencia_b, 64))
print("Sequência c):", proximo_elemento(sequencia_c, 7))
print("Sequência d):", proximo_elemento(sequencia_d, 64))
print("Sequência e):", proximo_elemento(sequencia_e, 6))
print("Sequência f):", proximo_elemento(sequencia_f, 19))