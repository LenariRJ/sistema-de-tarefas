from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADES = [
        ("BAIXA", "Baixa"),
        ("MEDIA", "Média"),
        ("ALTA", "Alta"),
    ]

    SITUACOES = [
        ("PENDENTE", "Pendente"),
        ("CONCLUIDA", "Concluída"),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADES
    )
    data_prevista = models.DateField()
    situacao = models.CharField(
        max_length=10,
        choices=SITUACOES,
        default="PENDENTE"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    def __str__(self):
        return self.titulo