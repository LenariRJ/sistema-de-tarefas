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


Autor: Leandro Nazareth Ribeiro
Matrícula: 202422923