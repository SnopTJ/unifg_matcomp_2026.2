f = {
    "TOMB-001": "Computador 01",
    "TOMB-002": "Computador 02",
    "TOMB-003": "Impressora 01",
    "TOMB-901": "Notebook 07", 
}

g = {
    "Computador 01": "Secretaria de Saúde",
    "Computador 02": "Secretaria de Educação",
    "Impressora 01": "Secretaria de Saúde",
    "Notebook 07": "Secretaria de Administração",
}

class TombamentoInexistenteError(Exception):
    """Levantado quando um tombamento não existe no domínio de f."""
    pass

class AtivoSemMapeamentoError(Exception):
    """Levantado quando f(tombamento) existe, mas g não define imagem para ele."""
    pass

def g_composta_f(tombamento: str) -> str:
    """
    Calcula (g ∘ f)(tombamento) = g(f(tombamento)).

    Levanta exceções específicas e informativas quando o pipeline
    não pode ser completado, em vez de deixar o programa quebrar
    com um KeyError genérico.
    """
    if tombamento not in f:
        raise TombamentoInexistenteError(
            f"Tombamento '{tombamento}' não existe no domínio de f (Tombamento -> Ativo)."
        )
    ativo = f[tombamento]

    if ativo not in g:
        raise AtivoSemMapeamentoError(
            f"Ativo '{ativo}' (obtido de f('{tombamento}')) não possui "
            f"secretaria mapeada em g (Ativo -> Secretaria)."
        )
    secretaria = g[ativo]

    return secretaria

print("=== Validando TOMB-901 ===")
try:
    resultado = g_composta_f("TOMB-901")
    print(f"(g ∘ f)('TOMB-901') = '{resultado}'")
    print(f"  Detalhe: f('TOMB-901') = '{f['TOMB-901']}' -> g('{f['TOMB-901']}') = '{resultado}'")
    print("  ✅ TOMB-901 processado com sucesso pelo pipeline.\n")
except (TombamentoInexistenteError, AtivoSemMapeamentoError) as erro:
    print(f"  ❌ Falha ao validar TOMB-901: {erro}\n")

print("=== Testando robustez do pipeline ===")
casos_de_teste = [
    "TOMB-001",
    "TOMB-901",
    "TOMB-999",
    "",
    None,         
]

for tombamento_teste in casos_de_teste:
    print(f"Testando tombamento: {tombamento_teste!r}")
    try:
        resultado = g_composta_f(tombamento_teste)
        print(f"  ✅ Sucesso: (g ∘ f)({tombamento_teste!r}) = '{resultado}'")
    except TombamentoInexistenteError as erro:
        print(f"  ⚠️  Tombamento inexistente: {erro}")
    except AtivoSemMapeamentoError as erro:
        print(f"  ⚠️  Ativo sem secretaria: {erro}")
    except Exception as erro:
        print(f"  ❌ Erro inesperado ({type(erro).__name__}): {erro}")
    print()

print("Pipeline testado com sucesso: nenhuma exceção não tratada quebrou a execução.")