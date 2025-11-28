'''1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , 
calcule e exiba    da coluna tempo_execucao, 
caso e o arquivo não exista ou houver erro na leitura,
mostre uma mensagem de erro.''' 

import csv

def ler_csv_calcular_metricas(arquivo_csv):
    try:
        tempos = []

        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)

            if 'tempo_execucao' not in leitor.fieldnames:
                print("Erro: A coluna 'tempo_execucao' não existe no arquivo.")
                return

            for linha in leitor:
                try:
                    valor = float(linha['tempo_execucao'])
                    tempos.append(valor)
                except ValueError:
                    print(f"Valor inválido encontrado: {linha['tempo_execucao']} (ignorado)")

        if not tempos:
            print("Nenhum valor válido encontrado na coluna 'tempo_execucao'.")
            return

        media = sum(tempos) / len(tempos)
        maximo = max(tempos)

        print(f"Média da coluna tempo_execucao: {media:.2f}")
        print(f"Valor máximo da coluna tempo_execucao: {maximo:.2f}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


nome_arquivo = "exemplo_tempo_execucao.csv"  # coloque o nome do seu arquivo CSV
ler_csv_calcular_metricas(nome_arquivo)