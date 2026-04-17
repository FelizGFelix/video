import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

video = []

def postar_video():
    limpar()
    nome = input("Digite o nome do vídeo: ")
    descricao = input("Digite a descrição do vídeo: ")
    canal ={
        "nome" : nome,
        "descricao" : descricao
    }
    video.append(canal)
    retorno()

def listar_video():
    limpar()
    for i in video:
        print("---------------------------------------")
        print("Nome: ", i["nome"])
        print("Descrição: ", i["descricao"])
        print("----------------------------------------")

def retorno():
    print("-------------------------------------------")
    input("Digite um valor para retornar: ")
    limpar()
    main()

def main():

    resposta = ""

    try:
        while resposta != 3:
            resposta = int(input("Digite uma das opções abaixo:\n 1 - Postar vídeo\n 2 - Acessar vídeos\n 3 - Sair\n-> "))

            if resposta == 1:
                postar_video()

            elif resposta == 2:
                listar_video()

            elif resposta == 3:
                limpar()
                print("Saindo do programa...")
                break

            else:
                print("Digite uma opção válida")
                retorno
    
    except:
        limpar()
        print("Digite uma opção válida")
        retorno()



if __name__ == "__main__":
    main()

