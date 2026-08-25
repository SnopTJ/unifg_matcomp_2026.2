Ativo = {"Computador 01", "Computador 02", "Impressora 01"}

Secretaria = {"Secretaria de Saúde", "Secretaria de Educação"}

f = {
    "Computador 01": "Secretaria de Saúde",
    "Computador 02": "Secretaria de Educação",
    "Impressora 01": "Secretaria de Saúde",     
}

assert set(f.keys()) == Ativo, "f não está definida para todos os elementos de Ativo!"

assert set(f.values()).issubset(Secretaria), "f possui imagem fora do contradomínio Secretaria!"

print("Função f: Ativo -> Secretaria")
for ativo, secretaria in f.items():
    print(f"  f({ativo}) = {secretaria}")
print()

imagens = list(f.values())
imagens_unicas = set(imagens)

e_injetora = len(imagens) == len(imagens_unicas)

print(f"Total de elementos no domínio (Ativo): {len(imagens)}")
print(f"Total de imagens distintas: {len(imagens_unicas)}")
print(f"f é injetora? {'Sim' if e_injetora else 'Não'}\n")

if not e_injetora:
    from collections import defaultdict
    grupos = defaultdict(list)
    for ativo, secretaria in f.items():
        grupos[secretaria].append(ativo)

    print("Contraexemplos (ativos diferentes com a mesma imagem):")
    for secretaria, ativos in grupos.items():
        if len(ativos) > 1:
            print(f"  {secretaria} recebe: {ativos}")
    print()

Im_f = imagens_unicas

print(f"Imagem Im(f) = {Im_f}")
print(f"|Im(f)| = {len(Im_f)} de {len(Secretaria)} secretarias do contradomínio\n")

e_sobrejetora = Im_f == Secretaria
print(f"f é sobrejetora? {'Sim' if e_sobrejetora else 'Não'}")

secretarias_nao_atingidas = Secretaria - Im_f
if secretarias_nao_atingidas:
    print(f"Secretarias sem nenhum ativo associado: {secretarias_nao_atingidas}")