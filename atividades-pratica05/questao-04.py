#4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.


from datetime import datetime

def dias_vivo(data_nascimento):

    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    
    hoje = datetime.now()
    
    diferenca = hoje - nascimento
    return diferenca.days


data = input("Digite sua data de nascimento (DD/MM/AAAA): ")

dias = dias_vivo(data)

print(f"\nVocê está vivo há aproximadamente {dias} dias.")