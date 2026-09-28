equipamentos = [
    {"id": "Respirador 1", "setor": "UTI", "dias": 45, "revisado": True},
    {"id": "Respirador 2", "setor": "UTI", "dias": 210, "revisado": True},
    {"id": "Bomba 1", "setor": "Triagem", "dias": 30, "revisado": False},
    {"id": "Monitor 1", "setor": "UTI", "dias": 100, "revisado": True},
]

todos_no_prazo = all(equipamento["dias"] <= 180 for equipamento in equipamentos)
if todos_no_prazo:
    print("Todos os equipamentos estão dentro do prazo de revisão.")

sem_revisao = any(not equipamento["revisado"] for equipamento in equipamentos)
if sem_revisao:
    print("Existem equipamentos que não foram revisados.")

id_problemas = [equipamento["id"] for equipamento in equipamentos if not equipamento["revisado"]]
for id in id_problemas:
    print(f"- {id}")