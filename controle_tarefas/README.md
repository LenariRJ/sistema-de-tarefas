Controle de Tarefas

Objetivo

Refatorar um protótipo de controle de tarefas utilizando uma classe `Tarefa`, funções e módulos separados.

## Execução

Com o Python instalado, execute no terminal:

python main.py

## Organização

* `tarefa.py`: contém a classe `Tarefa`, seus atributos e métodos.
* `servicos.py`: contém as funções de cadastro, listagem e filtro de tarefas.
* `main.py`: realiza a demonstração do programa e integra a classe com os serviços.

Funcionalidades

O programa demonstra:

* Cadastro de tarefas;
* Criação de objetos da classe `Tarefa`;
* Listagem das tarefas;
* Conclusão de uma tarefa;
* Filtro de tarefas pela situação.

Demonstração

O programa cria três tarefas, conclui a primeira e depois apresenta todas as tarefas e somente as tarefas concluídas.

Limitação

As tarefas permanecem apenas em memória durante a execução. Ao encerrar o programa, os dados são perdidos.

Autor: Leandro Nazareth Ribeiro
Matrícula: 202422923