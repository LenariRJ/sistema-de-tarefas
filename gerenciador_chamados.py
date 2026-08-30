chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Erro ao acessar e-mail",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador não liga",
        "prioridade": "alta",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Instalação de novo software",
        "prioridade": "baixa",
        "situacao": "fechado",
        "categoria": "software"
    },
    {
        "id": 6,
        "titulo": "Senha do sistema bloqueada",
        "prioridade": "média",
        "situacao": "aberto",
        "categoria": "acesso"
    }
]


print("=== TODOS OS CHAMADOS ===")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("-" * 30)


situacao_desejada = "aberto"
encontrou_chamado = False

print(f"\n=== CHAMADOS COM SITUAÇÃO: {situacao_desejada} ===")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Categoria: {chamado['categoria']}")
        print("-" * 30)
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado com essa situação.")


situacao_desejada = "cancelado"
encontrou_chamado = False

print(f"\n=== CHAMADOS COM SITUAÇÃO: {situacao_desejada} ===")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print("-" * 30)
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado com essa situação.")


id_chamado = 2
nova_situacao = "fechado"
encontrou_id = False

print(f"\n=== ATUALIZAÇÃO DO CHAMADO {id_chamado} ===")

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        encontrou_id = True
        print("Chamado atualizado com sucesso.")
        break

if not encontrou_id:
    print("Chamado não encontrado.")


id_chamado = 99
nova_situacao = "fechado"
encontrou_id = False

print(f"\n=== ATUALIZAÇÃO DO CHAMADO {id_chamado} ===")

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        encontrou_id = True
        print("Chamado atualizado com sucesso.")
        break

if not encontrou_id:
    print("Chamado não encontrado.")


categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("\n=== CATEGORIAS ATENDIDAS ===")

for categoria in categorias:
    print(f"- {categoria}")