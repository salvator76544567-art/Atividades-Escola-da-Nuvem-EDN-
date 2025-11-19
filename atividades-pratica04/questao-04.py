#4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def analisar_numeros():
    pares = 0
    impares = 0

  
    print("Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Digite um número: ")

        if entrada.lower() == "fim":
            break

        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if numero % 2 == 0:
            print(f"{numero} é PAR.")
            pares += 1
        else:
            print(f"{numero} é ÍMPAR.")
            impares += 1

    print("\n--- Resultado final ---")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


analisar_numeros()