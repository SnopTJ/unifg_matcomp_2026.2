f = {
    "TOMB-001": "Computador 01",
    "TOMB-002": "Computador 02",
    "TOMB-003": "Impressora 01",
}

Tombamento = set(f.keys())
Ativo = set(f.values())

print("Função original f: Tombamento -> Ativo")
for tomb, ativo in f.items():
    print(f"  f({tomb}) = {ativo}")
print()

imagens = list(f.values())
e_injetora = len(imagens) == len(set(imagens))

e_sobrejetora = set(imagens) == Ativo

e_bijetora = e_injetora and e_sobrejetora

print(f"f é injetora?   {'Sim' if e_injetora else 'Não'}")
print(f"f é sobrejetora? {'Sim' if e_sobrejetora else 'Não'}")
print(f"f é bijetora?    {'Sim' if e_bijetora else 'Não'}\n")

assert e_bijetora, "f precisa ser bijetora para que f⁻¹ exista como função!"

f_inversa = {ativo: tomb for tomb, ativo in f.items()}

print("Função inversa f⁻¹: Ativo -> Tombamento")
for ativo, tomb in f_inversa.items():
    print(f"  f⁻¹({ativo}) = {tomb}")
print()

imagens_inversa = list(f_inversa.values())
inversa_injetora = len(imagens_inversa) == len(set(imagens_inversa))
inversa_sobrejetora = set(imagens_inversa) == Tombamento
inversa_bijetora = inversa_injetora and inversa_sobrejetora

print(f"f⁻¹ é injetora?   {'Sim' if inversa_injetora else 'Não'}")
print(f"f⁻¹ é sobrejetora? {'Sim' if inversa_sobrejetora else 'Não'}")
print(f"f⁻¹ é bijetora?    {'Sim' if inversa_bijetora else 'Não'}\n")

verifica_ida = all(f_inversa[f[tomb]] == tomb for tomb in Tombamento)
verifica_volta = all(f[f_inversa[ativo]] == ativo for ativo in Ativo)

print(f"f⁻¹(f(x)) = x para todo x?  {'Sim' if verifica_ida else 'Não'}")
print(f"f(f⁻¹(y)) = y para todo y?  {'Sim' if verifica_volta else 'Não'}")

if verifica_ida and verifica_volta and inversa_bijetora:
    print("\n✅ f⁻¹ está corretamente construída e é bijetora.")