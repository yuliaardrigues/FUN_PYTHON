def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

numero = int(input("Informe um número: "))
fibonacci = fibonacci_sequence(numero)
print("Sequência de Fibonacci até", numero, ":", fibonacci)
