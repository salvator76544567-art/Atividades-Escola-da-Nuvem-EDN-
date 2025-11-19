'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

def calcular_desconto(preco, porcentagem):
   
    return preco * (porcentagem / 100)


def preco_final(preco, desconto):

    return preco - desconto


preco_produto = float(input("Digite o preço do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = calcular_desconto(preco_produto, porcentagem_desconto)
valor_final = preco_final(preco_produto, valor_desconto)

valor_desconto = round(valor_desconto, 2)
valor_final = round(valor_final, 2)

print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final do produto: R$ {valor_final:.2f}")
