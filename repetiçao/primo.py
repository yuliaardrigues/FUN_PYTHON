n = int(input())

if n < 2:
    print("O número não é primo.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")