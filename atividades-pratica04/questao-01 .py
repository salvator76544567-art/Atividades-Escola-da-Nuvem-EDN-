# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora():
    
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            return "Erro: divisão por zero!"
        resultado = num1 / num2
    else:
        return "Operador inválido!"

    return f"Resultado: {resultado}"

print(calculadora())