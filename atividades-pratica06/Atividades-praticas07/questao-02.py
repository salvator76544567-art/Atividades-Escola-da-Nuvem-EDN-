"""2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""

def criar_arquivo_pessoas():
    
    pessoas = [
        {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
        {"nome": "Bruno", "idade": 34, "cidade": "Rio de Janeiro"},
        {"nome": "Carlos", "idade": 22, "cidade": "Belo Horizonte"},
        {"nome": "Daniela", "idade": 30, "cidade": "Curitiba"},
    ]

    
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            
            arquivo.write(f"{'Nome':15}{'Idade':8}{'Cidade':20}\n")
            arquivo.write("-" * 40 + "\n")

            
            for p in pessoas:
                arquivo.write(f"{p['nome']:<15} {p['idade']:<8} {p['cidade']:<20}\n")

        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

    except Exception as erro:
        print(f"Falha ao salvar o arquivo: {erro}")


criar_arquivo_pessoas()