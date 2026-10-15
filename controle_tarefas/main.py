from tarefa import Tarefa
from servicos import cadastrar_tarefa, filtrar_por_situacao, listar_tarefas


tarefas = []


cadastrar_tarefa(
    tarefas,
    "Revisar chamados",
    "Verificar chamados pendentes da equipe",
    "Alta",
    Tarefa,
)

cadastrar_tarefa(
    tarefas,
    "Atualizar manual interno",
    "Ajustar instruções de atendimento",
    "Média",
    Tarefa,
)

cadastrar_tarefa(
    tarefas,
    "Planejar reunião",
    "Preparar pauta da reunião semanal",
    "Baixa",
    Tarefa,
)


# Concluir a primeira tarefa
tarefas[0].concluir()


print("=== Todas as tarefas ===")
listar_tarefas(tarefas)


print("\n=== Tarefas concluídas ===")
tarefas_concluidas = filtrar_por_situacao(tarefas, "Concluída")
listar_tarefas(tarefas_concluidas)