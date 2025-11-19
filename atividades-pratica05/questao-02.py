""""""

def eh_palindromo(texto):

    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())

    return texto_limpo == texto_limpo[::-1]


frase = input("Digite uma palavra ou frase: ")

resultado = eh_palindromo(frase)

if resultado:
    print("Sim")
else:
    print("Não")