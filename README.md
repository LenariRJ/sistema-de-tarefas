## Menu de Tarefas

O arquivo `menu_tarefas.py` implementa um protótipo de gerenciamento de tarefas pelo terminal.

### Execução

Com o ambiente virtual ativado, execute:

```bash
python menu_tarefas.py
```

### Opções disponíveis

* **1 - Cadastrar tarefa:** permite informar o título e a prioridade da tarefa.
* **2 - Listar tarefas:** apresenta todas as tarefas cadastradas, com número, prioridade e situação.
* **3 - Atualizar situação:** permite marcar uma tarefa existente como concluída.
* **4 - Encerrar sistema:** encerra o programa.

### Limitações

As tarefas são armazenadas somente em memória. Portanto, todos os registros são perdidos quando o programa é encerrado. O protótipo ainda não utiliza banco de dados nem interface web.

Semana 4 — Gerenciador de Chamados
Objetivo

Criar um protótipo em Python para gerenciamento de chamados internos, permitindo listar chamados, filtrar por situação, atualizar chamados por identificador e identificar categorias sem repetição.

Execução

Com o ambiente virtual ativado, execute:

python gerenciador_chamados.py
Funcionalidades
Listagem de todos os chamados;
Filtro de chamados por situação;
Atualização da situação de um chamado pelo ID;
Tratamento de chamado inexistente;
Identificação das categorias atendidas sem repetição utilizando set.
Exemplo de saída
ID: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Situação: aberto
Categoria: acesso
------------------------------

=== CATEGORIAS ATENDIDAS ===
- acesso
- hardware
- software
Autoria

Atividade realizada por: Leandro Nazareth Ribeiro.

Observação

Os chamados são armazenados apenas durante a execução do programa. Os dados não são salvos permanentemente em banco de dados ou arquivo.
## Hands-on — Primeira interface web com Django

### Objetivo

Criar a primeira interface web do Sistema de Gestão de Tarefas utilizando Django.

### Execução

Com o ambiente virtual ativado, execute:

```bash
python manage.py runserver
```

Depois, acesse no navegador:

* `/` — página inicial do sistema.
* `/tarefas/` — listagem inicial de tarefas.

### Organização

* `gestao_tarefas/`: configuração principal do projeto Django.
* `tarefas/`: aplicação responsável pelas tarefas.
* `tarefas/urls.py`: configuração das rotas da aplicação.
* `tarefas/views.py`: funções responsáveis pelas páginas.
* `tarefas/templates/tarefas/`: templates HTML.
* `manage.py`: arquivo utilizado para executar comandos do Django.

### Funcionalidades

O sistema apresenta:

* Página inicial;
* Listagem de tarefas;
* Título das tarefas;
* Prioridade;
* Situação;
* Navegação entre as páginas.

Os dados das tarefas são temporários e definidos diretamente na view, sem utilização de banco de dados.

## Semana 7 — Persistência de Categorias e Tarefas com Django

### Objetivo

Implementar a persistência das categorias e tarefas utilizando o banco de dados do Django.

### Implementações

- Criação do model `Categoria`;
- Criação do model `Tarefa`;
- Relacionamento entre `Tarefa` e `Categoria` com `ForeignKey`;
- Criação e aplicação das migrations;
- Registro dos models no Django Admin;
- Cadastro de 2 categorias;
- Cadastro de 2 tarefas;
- Consultas utilizando Django ORM;
- Atualização da situação de uma tarefa;
- Listagem das tarefas diretamente do banco de dados.

### Dados cadastrados

Categorias:
- Estudos
- Pessoal

Tarefas:
- Estudar Django
- Organizar atividades

### Consultas ORM realizadas

```python
Tarefa.objects.all()
Tarefa.objects.filter(situacao="PENDENTE")
Tarefa.objects.order_by("data_prevista")

Também foi realizada a atualização da situação de uma tarefa pendente para concluída utilizando:
tarefa = Tarefa.objects.filter(situacao="PENDENTE").first()tarefa.situacao = "CONCLUIDA"tarefa.save()


Dificuldade encontrada
A principal dificuldade foi adaptar o projeto para deixar de utilizar dados fixos na view e passar a buscar as tarefas diretamente do banco de dados.
Solução
Foram criados os models Categoria e Tarefa, realizadas as migrations e alterada a view de listagem para utilizar Tarefa.objects.all(). Dessa forma, os dados passaram a ser persistidos no banco de dados e continuam disponíveis após reiniciar o servidor.


Autor: Leandro Nazareth Ribeiro
Matrícula: 202422923