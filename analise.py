import csv
from collections import Counter
import matplotlib.pyplot as plt

idades = []
profissoes = []

with open("dados.csv", "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for pessoa in leitor:
        idade = int(pessoa["Idade"])
        profissao = pessoa["Profissão"].strip()

        idades.append(idade)
        profissoes.append(profissao)

quantidade_pessoas = len(idades)
media_idade = sum(idades) / quantidade_pessoas
idade_mais_nova = min(idades)
idade_mais_velha = max(idades)

contagem_profissoes = Counter(profissoes)

print("\nRELATÓRIO DOS DADOS")
print("-------------------")
print("Quantidade de pessoas cadastradas:", quantidade_pessoas)
print("Média de idade:", round(media_idade, 1))
print("Menor idade:", idade_mais_nova)
print("Maior idade:", idade_mais_velha)

print("\nQUANTIDADE POR PROFISSÃO")
print("------------------------")

for profissao, quantidade in contagem_profissoes.items():
    print(f"{profissao}: {quantidade}")

profissoes_lista = list(contagem_profissoes.keys())
quantidades_lista = list(contagem_profissoes.values())

plt.figure(figsize=(10, 6))
plt.bar(profissoes_lista, quantidades_lista)

plt.title("Quantidade de pessoas por profissão")
plt.xlabel("Profissão")
plt.ylabel("Quantidade")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("grafico_profissoes.png")
plt.show()