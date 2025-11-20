"""1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente."""

import random
import string

def gerar_senha(tamanho):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    if tamanho <= 0:
        print("O tamanho deve ser um número positivo!")
    else:
        senha = gerar_senha(tamanho)
        print("Senha gerada:", senha)
except ValueError:
    print("Por favor, digite um número válido!")