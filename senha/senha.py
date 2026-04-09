senha = ""
senhacorreta = 1234
limite = 3
contador = 0

while senha != senhacorreta:
    senha = int(input("Digite sua senha: "))

    if senha != senhacorreta:
        print("Senha errada, tente novamente!")
        contador += 1

        if contador == 3:
            print("Tentativa máxima excedida!")
            break

    else:
        print("Acesso liberado!")