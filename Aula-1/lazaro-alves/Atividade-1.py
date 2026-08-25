from itertools import product
from collections import Counter

A = {"CRAS", "Escola", "Postinho"}

B = {"Boa Viagem", "Casa Amarela", "Ibura"}

print("Conjunto A (Equipamentos):")
print(A, "\n")

print("Conjunto B (Bairros):")
print(B, "\n")

produto_cartesiano = set(product(A, B))

print(f"Produto cartesiano A x B possui {len(produto_cartesiano)} pares:")
for par in sorted(produto_cartesiano):
    print(par)
print()

relacao_atendimento = {
    ("CRAS", "Boa Viagem"),
    ("Escola", "Ibura"),
    ("Postinho", "Casa Amarela"),
}

assert relacao_atendimento.issubset(produto_cartesiano), \
    "A relação de atendimento contém pares que não pertencem a A x B!"

print(f"Relação de atendimento (R \u2286 A x B) possui {len(relacao_atendimento)} pares:")
for par in sorted(relacao_atendimento):
    print(f"  {par[0]} atende o bairro {par[1]}")
print()

nao_atendidos = produto_cartesiano - relacao_atendimento
print(f"Pares possíveis mas SEM atendimento: {len(nao_atendidos)}")

equipamento_counts = Counter(e for e, b in relacao_atendimento)
print("\nQuantidade de bairros atendidos por equipamento:")
for equipamento in sorted(A):
    print(f"  {equipamento}: {equipamento_counts.get(equipamento, 0)} bairro(s)")

bairro_counts = Counter(b for e, b in relacao_atendimento)
print("\nQuantidade de equipamentos que atendem cada bairro:")
for bairro in sorted(B):
    print(f"  {bairro}: {bairro_counts.get(bairro, 0)} equipamento(s)")
