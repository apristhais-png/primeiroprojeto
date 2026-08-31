import csv
import os

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
profissao = input("Qual é a sua profissão? ")

arquivo = "dados.csv"

arquivo_existe = os.path.exists(arquivo)

with open(arquivo, "a", newline="", encoding="utf-8-sig") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";")

    if not arquivo_existe:
        escritor.writerow(["Nome", "Idade", "Profissão"])

    escritor.writerow([nome, idade, profissao])

print("\nDados salvos com sucesso no arquivo dados.csv!")
