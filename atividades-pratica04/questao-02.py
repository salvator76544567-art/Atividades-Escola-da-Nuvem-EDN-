#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def registrar_notas():
    notas = []
    
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

        if entrada.lower() == "fim":
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite uma nota numérica.")
    
    if len(notas) == 0:
        print("Nenhuma nota registrada.")
    else:
        media = sum(notas) / len(notas)
        print(f"\nNotas registradas: {notas}")
        print(f"Média da turma: {media:.2f}")



registrar_notas()

