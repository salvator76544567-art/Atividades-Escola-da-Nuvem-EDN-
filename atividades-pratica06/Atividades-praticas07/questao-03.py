"""3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
"""

def ler_arquivo():
    
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            print("\n---- Conteúdo do arquivo ----\n")
            for linha in arquivo:
                print(linha, end="")  
            print("\n------------------------------")

    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as erro:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {erro}")



ler_arquivo()