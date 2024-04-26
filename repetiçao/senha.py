senha = input("Senha: ")

senha_correta = "senha123"

for i in range(3):
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        print("Senha incorreta.")
