from django.db import models

class Reclamacao(models.Model):
    STATUS_CHOICES = [
        ('NAO_RESPONDIDA' , 'Não Respondida'),
        ('RESPONDIDA', 'Respondida')
    ]

    URGENCIA_CHOICES = [
        ('NAO_URGENTE', 'Não Urgente'),
        ('URGENTE', 'Urgente')
    ]

    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NAO_RESPONDIDA')
    data_reclamacao = models.DateTimeField(auto_now_add=True)
    urgencia = models.CharField(max_length=20, choices=URGENCIA_CHOICES, default='NAO_URGENTE')


    def __str__(self):
        return self.titulo

