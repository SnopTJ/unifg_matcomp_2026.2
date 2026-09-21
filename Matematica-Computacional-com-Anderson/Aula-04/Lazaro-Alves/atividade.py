from itertools import product


def alarme(porta, ignicao, farois):
	"""Retorna 1 quando uma das regras de ativacao do alarme e atendida."""
	return int((farois and not ignicao) or (porta and ignicao))

print("A B C | S")
print("------|---")
minitermos = []
for porta, ignicao, farois in product((0, 1), repeat=3):
	saida = alarme(porta, ignicao, farois)
	if saida:
		minitermos.append(4 * porta + 2 * ignicao + farois)
	print(f"{porta} {ignicao} {farois} | {saida}")

print(f"Minitermos de S: {minitermos}")
