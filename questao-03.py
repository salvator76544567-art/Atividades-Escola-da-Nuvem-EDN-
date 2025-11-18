"""" 
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.  
""""

while True: 
    senha = input("Digite a sua senha:")
    
    if senha.lower () == "sair":
        print("Encerrando o programa.")
        break

    tem_oito_caracteres = len(senha) >= 8

    tem_numero = any(caractere.isdigit() for caractere in senha)

    eh_forte = tem_oito_caracteres and tem_numero
    if eh_forte:
        print("Parabens, sua senha corresponde aos requisitos minimos de uma senha segura.")
    else:
        print("Que pena, sua senha não corresponde aos requisitos minimos .")

        if not tem_oito_caracteres:
            print(" Sua senha deve conter pelo menos 8 caracteres, tente novamente.")

        if not tem_numero:
            print(" Sua senha deve conter pelo menos 1 numero, tente novamente.")
