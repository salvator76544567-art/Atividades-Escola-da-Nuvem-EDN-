"""3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha."""

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status() 

        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado. Verifique e tente novamente.")
            return

        print("Logradouro:", dados.get("logradouro", "Não informado"))
        print("Bairro:", dados.get("bairro", "Não informado"))
        print("Cidade:", dados.get("localidade", "Não informado"))
        print("Estado:", dados.get("uf", "Não informado"))

    except requests.exceptions.RequestException:
        print("Falha ao conectar à API. Tente novamente mais tarde.")
    
cep = input("Digite um CEP (somente números): ").strip()

if len(cep) == 8 and cep.isdigit():
    consultar_cep(cep)
else:
    print("CEP inválido! Digite exatamente 8 números.")