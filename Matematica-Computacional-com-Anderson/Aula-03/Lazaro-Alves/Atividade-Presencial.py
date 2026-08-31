def decidir_sinal_verde(ambulancia: bool, fluxo_alto: bool, pedestre: bool, cancela_trem: bool) -> bool:
    if cancela_trem:
        return False
    if ambulancia:
        return True
    return fluxo_alto and not pedestre

assert decidir_sinal_verde(True, True, False, False) == True
assert decidir_sinal_verde(False, True, False, False) == True
assert decidir_sinal_verde(False, True, True, False) == False
assert decidir_sinal_verde(True, True, False, True) == False
assert decidir_sinal_verde(False, False, False, False) == False
print("SUCESSO: TODAS AS REGRAS LÓGICAS HOMOLOGADAS!")