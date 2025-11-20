"""2 - Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha."""

import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  

        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("Usuário encontrado:")
        print("Nome:", nome)
        print("E-mail:", email)
        print("País:", pais)

    except requests.exceptions.RequestException:
        print("Falha ao conectar à API. Tente novamente mais tarde.")

buscar_usuario()