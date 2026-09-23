from django.db import models
from django.utils import timezone

# Create your models here.

class Aluno(models.Model):
    matricula =  models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.nome}'

class Professor(models.Model):
    disciplina =  models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.nome}'

class Turma(models.Model):
    turma = models.CharField(max_length=15)
    turno = models.CharField(max_length=15)
    professor_fk = models.CharField(max_length=15)
    aluno_fk = models.CharField(max_length=15)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)

    def __str__(self):
            return f'{self.turma}'



      
      




    

