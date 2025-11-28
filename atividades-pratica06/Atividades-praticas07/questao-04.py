"""4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""

import json

def salvar_e_ler_json():
    
    dados = {
        "nome": "Maria",
        "idade": 29,
        "cidade": "Fortaleza"
    }

    nome_arquivo = input("Digite o nome do arquivo JSON para salvar (ex: dados.json): ")

    
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as erro:
        print(f"Falha ao salvar o arquivo: {erro}")
        return  

    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados_lidos = json.load(arquivo)

        print("\n--- Conteúdo do arquivo JSON ---")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")
        print("--------------------------------")

    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as erro:
        print(f"Erro ao ler o arquivo JSON: {erro}")



salvar_e_ler_json()