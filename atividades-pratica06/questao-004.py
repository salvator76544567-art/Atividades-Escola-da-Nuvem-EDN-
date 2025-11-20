"""4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.  """

import requests

def consultar_moeda(moeda):
    moeda = moeda.upper() 
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Moeda não encontrada! Verifique o código da moeda.")
            return

        info = dados[chave]

        print(f"\n Cotação {moeda} → BRL")
        print("Valor atual:", info["bid"])
        print("Máxima do dia:", info["high"])
        print("Mínima do dia:", info["low"])
        print("Última atualização:", info["create_date"])

    except requests.exceptions.RequestException:
        print("Erro ao conectar à API. Tente novamente mais tarde.")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip()

if moeda.isalpha() and len(moeda) == 3:
    consultar_moeda(moeda)
else:
    print("Código de moeda inválido! Use 3 letras, ex: USD.")